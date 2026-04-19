import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Page Object для страницы калькулятора с задержкой (slow-calculator)."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 50)

        self.delay_input: tuple = (By.CSS_SELECTOR, "#delay")
        self.screen: tuple = (By.CSS_SELECTOR, ".screen")
        self.calculator: tuple = (By.CSS_SELECTOR, "#calculator")

        self.digit_buttons: dict = {
            '0': (By.XPATH, "//span[text()='0']"),
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
        }

        self.operator_buttons: dict = {
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='*']"),
            '/': (By.XPATH, "//span[text()='/']"),
            '=': (By.XPATH, "//span[text()='=']"),
        }

    @allure.step("Ожидание загрузки калькулятора")
    def wait_for_calculator(self) -> "CalculatorPage":
        """
        Ожидает загрузки калькулятора на странице.
        """
        self.wait.until(EC.presence_of_element_located(self.calculator))
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: str) -> "CalculatorPage":
        """
        Устанавливает значение задержки в поле ввода.
        """
        delay_input = self.wait.until(EC.element_to_be_clickable(
            self.delay_input))
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    @allure.step("Нажать цифру {digit}")
    def click_digit(self, digit: int) -> "CalculatorPage":
        """
        Нажимает кнопку с указанной цифрой.
        """
        digit_str: str = str(digit)
        button = self.wait.until(EC.element_to_be_clickable(
            self.digit_buttons[digit_str]))
        button.click()
        return self

    @allure.step("Нажать оператор {operator}")
    def click_operator(self, operator: str) -> "CalculatorPage":
        """
        Нажимает кнопку с математическим оператором.
        """
        if operator not in self.operator_buttons:
            raise ValueError(f"Некорректный оператор: {operator}")

        button = self.wait.until(
            EC.element_to_be_clickable(self.operator_buttons[operator])
        )
        button.click()
        return self

    @allure.step("Нажать равно (=)")
    def click_equals(self) -> "CalculatorPage":
        """
        Нажимает кнопку равно.
        """
        return self.click_operator('=')

    @allure.step("Получить результат с экрана")
    def get_result(self) -> str:
        """
        Получает текст результата с экрана калькулятора.
        """
        screen = self.wait.until(EC.presence_of_element_located(self.screen))
        return screen.text

    @allure.step("Ожидать результат {expected_result} на экране")
    def wait_for_result(self, expected_result: str) -> "CalculatorPage":
        """
        Ожидает появления ожидаемого результата на экране.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_result)
        )
        return self
