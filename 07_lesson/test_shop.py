import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from PagesShop.LoginPage import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_saucedemo_compact(driver):
    items_to_add = ["backpack", "bolt-tshirt", "onesie"]

    summary_page = (LoginPage(driver)
                    .wait_for_page_load()
                    .login_as("standard_user", "secret_sauce")
                    .wait_for_page_load()
                    .add_multiple_items(*items_to_add)
                    .go_to_cart()
                    .wait_for_page_load()
                    .click_checkout()
                    .wait_for_page_load()
                    .fill_shipping_info("Elina", "Ushakova", "123456")
                    .click_continue()
                    .wait_for_page_load())

    total = summary_page.get_total_value()
    expected_total = 58.29

    assert round(total, 2) == expected_total, \
        f"Ожидалось ${expected_total}, получено ${total}"
