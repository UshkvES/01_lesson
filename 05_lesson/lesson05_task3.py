from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=Service
                           (GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

sleep(2)

input_field = driver.find_element(By.TAG_NAME, "input")

driver.execute_script("arguments[0].type = 'text';", input_field)

input_field.send_keys("Sky", Keys.RETURN)
sleep(5)

input_field.clear()
sleep(3)

input_field.send_keys("Pro", Keys.RETURN)

sleep(5)

driver.quit()
