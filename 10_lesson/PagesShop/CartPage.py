import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        self.cart_list: tuple = (By.CSS_SELECTOR, ".cart_list")
        self.checkout_button: tuple = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Ожидание загрузки страницы корзины")
    def wait_for_page_load(self) -> "CartPage":
        """
        Ожидает загрузки списка товаров в корзине.
        """
        self.wait.until(EC.presence_of_element_located(self.cart_list))
        return self

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self):
        """
        Нажимает кнопку оформления заказа.
        """
        button = self.wait.until(EC.element_to_be_clickable(
            self.checkout_button))
        button.click()
        from PagesShop.CheckoutPage import CheckoutPage
        return CheckoutPage(self.driver)
