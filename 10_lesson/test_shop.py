import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from PagesShop.LoginPage import LoginPage


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Firefox.
    """
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.epic("Интернет-магазин SauceDemo")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Проверка итоговой суммы в корзине")
@allure.description(
    "Тест проверяет корректность расчета итоговой суммы заказа. "
    "Пользователь авторизуется, добавляет в корзину товары: "
    "backpack, bolt-tshirt, onesie, оформляет заказ и сравнивает "
    "полученную итоговую сумму с ожидаемой (58.29)."
)
class TestShop:

    @allure.id("TC-SHOP-001")
    @allure.story("Расчет итоговой суммы")
    def test_saucedemo_checkout_total(self, driver: WebDriver) -> None:
        """
        Тест проверяет корректность итоговой суммы при оформлении заказа.
        """
        items_to_add = ["backpack", "bolt-tshirt", "onesie"]
        expected_total = 58.29

        with allure.step("Авторизация на сайте"):
            summary_page = (
                LoginPage(driver)
                .wait_for_page_load()
                .login_as("standard_user", "secret_sauce")
            )

        with allure.step("Добавление товаров в корзину"):
            summary_page = (
                summary_page
                .wait_for_page_load()
                .add_multiple_items(*items_to_add)
            )

        with allure.step("Переход в корзину и оформление заказа"):
            summary_page = (
                summary_page
                .go_to_cart()
                .wait_for_page_load()
                .click_checkout()
                .wait_for_page_load()
                .fill_shipping_info("Elina", "Ushakova", "123456")
                .click_continue()
                .wait_for_page_load()
            )

        with allure.step("Получение итоговой суммы"):
            total = summary_page.get_total_value()

        with allure.step(f"Проверяем, итоговая сумма равна ${expected_total}"):
            assert round(total, 2) == expected_total, \
                f"Ожидалось ${expected_total}, получено ${total}"

        allure.attach(
            f"Итоговая сумма: ${total}",
            "Результат",
            allure.attachment_type.TEXT
        )
