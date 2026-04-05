from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.first_name_input = (By.CSS_SELECTOR, "#first-name")
        self.last_name_input = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_input = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.checkout_info_container = (
            By.CSS_SELECTOR, ".checkout_info_container")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(
            self.checkout_info_container))
        return self

    def enter_first_name(self, first_name: str):
        element = self.wait.until(EC.element_to_be_clickable(
            self.first_name_input))
        element.clear()
        element.send_keys(first_name)
        return self

    def enter_last_name(self, last_name: str):
        element = self.wait.until(EC.element_to_be_clickable(
            self.last_name_input))
        element.clear()
        element.send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code: str):
        element = self.wait.until(EC.element_to_be_clickable(
            self.postal_code_input))
        element.clear()
        element.send_keys(postal_code)
        return self

    def fill_shipping_info(
            self, first_name: str, last_name: str, postal_code: str):
        return (self
                .enter_first_name(first_name)
                .enter_last_name(last_name)
                .enter_postal_code(postal_code))

    def click_continue(self):
        button = self.wait.until(EC.element_to_be_clickable(
            self.continue_button))
        button.click()
        from PagesShop.CheckoutSummaryPage import CheckoutSummaryPage
        return CheckoutSummaryPage(self.driver)
