from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.inventory_container = (By.CSS_SELECTOR, "#inventory_container")
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

        self.add_to_cart_buttons = {
            "backpack": (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"),
            "bolt-tshirt": (
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"),
            "bike-light": (
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light"),
            "fleece-jacket": (
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket"),
            "tatt-red": (
                By.CSS_SELECTOR, "#add-to-cart-test.allthethings()-t-shirt-("
                "red)")}

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(
            self.inventory_container))
        return self

    def add_item_to_cart(self, item_key: str):
        if item_key not in self.add_to_cart_buttons:
            raise ValueError(f"Неизвестный товар: {
                item_key}. Доступные товары: {
                    list(self.add_to_cart_buttons.keys())}")

        button = self.wait.until(EC.element_to_be_clickable(
            self.add_to_cart_buttons[item_key]))
        button.click()

    def add_multiple_items(self, *item_keys):
        for item_key in item_keys:
            self.add_item_to_cart(item_key)
        return self

    def go_to_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        cart_link.click()
        from PagesShop.CartPage import CartPage
        return CartPage(self.driver)
