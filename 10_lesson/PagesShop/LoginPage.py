import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        self.username_input: tuple = (By.CSS_SELECTOR, "#user-name")
        self.password_input: tuple = (By.CSS_SELECTOR, "#password")
        self.login_button: tuple = (By.CSS_SELECTOR, "#login-button")
        self.login_box: tuple = (By.CSS_SELECTOR, ".login-box")

    @allure.step("Ожидание загрузки страницы логина")
    def wait_for_page_load(self) -> "LoginPage":
        """
        Ожидает загрузки формы логина.
        """
        self.wait.until(EC.presence_of_element_located(self.login_box))
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> "LoginPage":
        """
        Вводит имя пользователя в соответствующее поле.
        """
        element = self.wait.until(EC.element_to_be_clickable(
            self.username_input))
        element.clear()
        element.send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> "LoginPage":
        """
        Вводит пароль в соответствующее поле.
        """
        element = self.wait.until(EC.element_to_be_clickable(
            self.password_input))
        element.clear()
        element.send_keys(password)
        return self

    @allure.step("Нажать кнопку Login")
    def click_login(self):
        """
        Нажимает кнопку логина и переходит на главную страницу.
        """
        element = self.wait.until(EC.element_to_be_clickable(
            self.login_button))
        element.click()
        from PagesShop.MainPage import MainPage
        return MainPage(self.driver)

    @allure.step("Авторизоваться как {username}")
    def login_as(self, username: str, password: str):
        """
        Выполняет полную авторизацию с указанными учетными данными.
        """
        return (self
                .enter_username(username)
                .enter_password(password)
                .click_login())
