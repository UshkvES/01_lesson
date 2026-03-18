from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service
                           (GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10)


def test_buy():
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-box")))

    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Elina")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Ushakova")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total_element = wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text
    actual_total = total_text.split('$')[-1].strip()

    driver.quit()

    expected_total = "58.29"
    assert actual_total == expected_total, \
        f"Ожидалось ${expected_total}, получено ${actual_total}"
    print("Проверка пройдена: сумма корректна")


if __name__ == "__main__":
    test_buy()
