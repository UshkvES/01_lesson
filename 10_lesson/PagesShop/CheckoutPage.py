import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page Object для страницы ввода информации о доставке."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        self.first_name_input: tuple = (By.CSS_SELECTOR, "#first-name")
        self.last_name_input: tuple = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_input: tuple = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button: tuple = (By.CSS_SELECTOR, "#continue")
        self.checkout_info_container: tuple = (
            By.CSS_SELECTOR, ".checkout_info_container")

    @allure.step("Ожидание загрузки страницы оформления заказа")
    def wait_for_page_load(self) -> "CheckoutPage":
        """
        Ожидает загрузки контейнера с формой ввода.
        """
        self.wait.until(EC.presence_of_element_located(
            self.checkout_info_container))
        return self

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name: str) -> "CheckoutPage":
        """
        Вводит имя в соответствующее поле.
        """
        element = self.wait.until(EC.element_to_be_clickable(
            self.first_name_input))
        element.clear()
        element.send_keys(first_name)
        return self

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name: str) -> "CheckoutPage":
        """
        Вводит фамилию в соответствующее поле.
        """
        element = self.wait.until(EC.element_to_be_clickable(
            self.last_name_input))
        element.clear()
        element.send_keys(last_name)
        return self

    @allure.step("Ввести почтовый индекс: {postal_code}")
    def enter_postal_code(self, postal_code: str) -> "CheckoutPage":
        """
        Вводит почтовый индекс в соответствующее поле.
        """
        element = self.wait.until(EC.element_to_be_clickable(
            self.postal_code_input))
        element.clear()
        element.send_keys(postal_code)
        return self

    @allure.step(
        "Заполнить информацию о доставке: "
        "{first_name} {last_name}, {postal_code}")
    def fill_shipping_info(self, first_name: str, last_name: str,
                           postal_code: str) -> "CheckoutPage":
        """
        Заполняет все поля информации о доставке.
        """
        return (self
                .enter_first_name(first_name)
                .enter_last_name(last_name)
                .enter_postal_code(postal_code))

    @allure.step("Нажать кнопку Continue")
    def click_continue(self):
        """
        Нажимает кнопку продолжения.
        """
        button = self.wait.until(EC.element_to_be_clickable(
            self.continue_button))
        button.click()
        from PagesShop.CheckoutSummaryPage import CheckoutSummaryPage
        return CheckoutSummaryPage(self.driver)
