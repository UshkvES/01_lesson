from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutSummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.summary_container = (
            By.CSS_SELECTOR, ".checkout_summary_container")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(self.summary_container))
        return self

    def get_total_text(self) -> str:
        element = self.wait.until(EC.presence_of_element_located(
            self.total_label))
        return element.text

    def get_total_value(self) -> float:
        total_text = self.get_total_text()
        value_str = total_text.replace("Total:", "").replace("$", "").strip()
        return float(value_str)
