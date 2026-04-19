import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutSummaryPage:
    """Page Object для страницы итогов заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы итогов заказа.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        self.summary_container: tuple = (
            By.CSS_SELECTOR, ".checkout_summary_container")
        self.total_label: tuple = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Ожидание загрузки страницы итогов заказа")
    def wait_for_page_load(self) -> "CheckoutSummaryPage":
        """
        Ожидает загрузки контейнера с итогами заказа.
        """
        self.wait.until(EC.presence_of_element_located(self.summary_container))
        return self

    @allure.step("Получить текст с общей суммой")
    def get_total_text(self) -> str:
        """
        Получает текст с отображением общей суммы.
        """
        element = self.wait.until(EC.presence_of_element_located(
            self.total_label))
        return element.text

    @allure.step("Получить числовое значение общей суммы")
    def get_total_value(self) -> float:
        """
        Извлекает числовое значение общей суммы из текста.
        """
        total_text: str = self.get_total_text()
        value_str: str = total_text.replace(
            "Total:", "").replace("$", "").strip()
        return float(value_str)
