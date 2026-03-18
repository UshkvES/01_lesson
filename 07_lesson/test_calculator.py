import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PagesCalculator.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = CalculatorPage(driver)
    calculator.wait_for_calculator()
    (calculator
     .set_delay("45")
     .click_digit(7)
     .click_operator('+')
     .click_digit(8)
     .click_equals()
     .wait_for_result("15"))

    result = calculator.get_result()
    assert result == "15", f"Ожидался результат 15, получен: {result}"
    print(f"Результат: {result}")
