from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service
                          (ChromeDriverManager
                           (chrome_type=ChromeType.GOOGLE).install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

sleep(5)

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

blue_button.click()

sleep(5)

driver.quit()
