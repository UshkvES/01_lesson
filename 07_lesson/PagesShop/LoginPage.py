from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_input = (By.CSS_SELECTOR, "#user-name")
        self.password_input = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")
        self.login_box = (By.CSS_SELECTOR, ".login-box")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(self.login_box))
        return self

    def enter_username(self, username: str):
        element = self.wait.until(EC.element_to_be_clickable(
            self.username_input))
        element.clear()
        element.send_keys(username)
        return self

    def enter_password(self, password: str):
        element = self.wait.until(EC.element_to_be_clickable(
            self.password_input))
        element.clear()
        element.send_keys(password)
        return self

    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable(
            self.login_button))
        element.click()
        from PagesShop.MainPage import MainPage
        return MainPage(self.driver)

    def login_as(self, username: str, password: str):
        return (self
                .enter_username(username)
                .enter_password(password)
                .click_login())
