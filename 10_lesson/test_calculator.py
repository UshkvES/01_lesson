import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from PagesCalculator.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Chrome.
    """
    driver: WebDriver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@allure.epic("Калькулятор")
@allure.feature("Арифметические операции")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения с задержкой")
@allure.description(
    "Тест проверяет работу калькулятора с установленной задержкой. "
    "Устанавливается задержка 45 секунд, выполняется операция 7+8, "
    "ожидается результат 15.")
class TestCalculator:

    @allure.id("TC-CALC-001")
    @allure.story("Сложение чисел")
    def test_calculator_addition(self, driver: WebDriver) -> None:
        """
        Тест проверяет операцию сложения на калькуляторе с задержкой.
        """
        with allure.step("Инициализировать страницу калькулятора"):
            calculator: CalculatorPage = CalculatorPage(driver)

        with allure.step("Ожидать загрузки калькулятора"):
            calculator.wait_for_calculator()

        with allure.step("Выполнить действия: задержка 45, нажать 7, +, 8, ="):
            (calculator
             .set_delay("45")
             .click_digit(7)
             .click_operator('+')
             .click_digit(8)
             .click_equals())

        with allure.step("Ожидать появления результата '15' на экране"):
            calculator.wait_for_result("15")

        with allure.step("Получить результат с экрана"):
            result: str = calculator.get_result()

        with allure.step("Проверить, что результат равен '15'"):
            assert result == "15", f"Ожидался результат 15, получен: {result}"

        allure.attach(f"Результат вычисления: {result}", "Результат",
                      allure.attachment_type.TEXT)
