from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service
                           (GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

sleep(2)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

sleep(2)

success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")

message_text = success_message.text
print(message_text)

sleep(3)

driver.quit()
