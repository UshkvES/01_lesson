from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )
input_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(f"{button_text}")

driver.quit()
