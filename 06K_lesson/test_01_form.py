from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_fields_validation():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
        }

    for field_name, value in fields.items():
        field = driver.find_element(By.NAME, field_name)
        field.clear()
        field.send_keys(value)

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#zip-code.alert")))

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    zip_code_class = zip_code_field.get_attribute("class")
    assert "alert-danger" in zip_code_class, (
            f"Zip code должен иметь класс alert-danger, получен: {
                zip_code_class}"
            )
    print("Zip code: КРАСНЫЙ (правильно)")

    success_fields = [
        "#first-name", "#last-name", "#address", "#e-mail",
        "#phone", "#city", "#country", "#job-position", "#company"
    ]

    for field_selector in success_fields:
        field = driver.find_element(By.CSS_SELECTOR, field_selector)
        field_class = field.get_attribute("class")
        assert "alert-success" in field_class, (
            f"Поле {field_selector} должно иметь класс alert-success, "
            f"получен: {field_class}"
            )
    print(f"{field_selector:15}: ЗЕЛЕНЫЙ (правильно)")

    driver.quit()


if __name__ == "__main__":
    test_form_fields_validation()
