from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.calculator = (By.CSS_SELECTOR, "#calculator")

        self.digit_buttons = {
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

        self.operator_buttons = {
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='*']"),
            '/': (By.XPATH, "//span[text()='/']"),
            '=': (By.XPATH, "//span[text()='=']"),
        }

        self.button_by_text = "//span[text()='{}']"

    def wait_for_calculator(self):
        self.wait.until(EC.presence_of_element_located(
            self.calculator))
        return self

    def set_delay(self, seconds: str):
        delay_input = self.wait.until(EC.element_to_be_clickable(
            self.delay_input))
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_digit(self, digit):
        digit_str = str(digit)
        button = self.wait.until(EC.element_to_be_clickable(
            self.digit_buttons[digit_str]))
        button.click()
        return self

    def click_operator(self, operator):
        if operator not in self.operator_buttons:
            raise ValueError(f"Некорректный оператор: {operator}")

        button = self.wait.until(
            EC.element_to_be_clickable(self.operator_buttons[operator])
        )
        button.click()
        return self

    def click_equals(self):
        return self.click_operator('=')

    def get_result(self) -> str:
        screen = self.wait.until(
            EC.presence_of_element_located(self.screen))
        return screen.text

    def wait_for_result(self, expected_result: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_result))
        return self
