from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))


def test_calculator():
    wait = WebDriverWait(driver, 45)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "#calculator")))

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[text()='7']")))
    button_7.click()

    button_plus = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[text()='+']")))
    button_plus.click()

    button_8 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[text()='8']")))
    button_8.click()

    button_equals = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[text()='=']")))
    button_equals.click()

    result_locator = (By.CSS_SELECTOR, ".screen")
    wait.until(EC.text_to_be_present_in_element(result_locator, "15"))

    result_text = driver.find_element(*result_locator).text
    assert result_text == "15", f"Ожидался результат 15, получен: {
        result_text}"
    print(f"Результат: {result_text} (правильно)")

    driver.quit()


if __name__ == "__main__":
    test_calculator()
