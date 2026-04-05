from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cart_list = (By.CSS_SELECTOR, ".cart_list")
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(self.cart_list))
        return self

    def click_checkout(self):
        button = self.wait.until(EC.element_to_be_clickable(
            self.checkout_button))
        button.click()
        from PagesShop.CheckoutPage import CheckoutPage
        return CheckoutPage(self.driver)
