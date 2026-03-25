from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure

from pages_shop.LoginPage import LoginPage
from pages_shop.MainPage import MainPage
from pages_shop.CartPage import CartPage
from pages_shop.CheckPage import CheckPage


@allure.title("Покупка товаров на SauseDemo")
@allure.description("Тестирование полного пользовательского пути покупки товаров: авторизация, добавление в корзину, оформление заказа и проверка итоговой стоимости")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_with_page_objects():
    with allure.step("Открытие браузера и переход на сайт магазина"):
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    check_page = CheckPage(driver)

    with allure.step("Авторизация пользователя {standart_user}: {secret_sauce}"):
        login_page.login("standard_user", "secret_sauce")
        allure.attach(driver.get_full_page_screenshot_as_png(), name="После авторизации", attachment_type=allure.attachment_type.PNG)

    goods_to_buy = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    with allure.step("Добавление товаров в корзину"):
        for good_id in goods_to_buy:
            main_page.add_to_cart(good_id)

    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
        allure.attach(driver.get_full_page_screenshot_as_png(), name="Страница корзины", attachment_type=allure.attachment_type.PNG)

    with allure.step("Переход на страницу оформления заказа"):
        cart_page.checkout()

    with allure.step("Заполнение форма заказа данными пользователя"):
        check_page.fill_form("Natalya", "Evdokimova", "412365")

    with allure.step("Получение итоговой стоимости корзины"):
        total_text = check_page.get_total_price()
        allure.attach(driver.get_full_page_screenshot_as_png(), name="Страница подтверждения заказа", attachment_type=allure.attachment_type.PNG)

    with allure.step("Закрытие браузера"):
        driver.quit()

    with allure.step("Проверка, что итоговая стоимость корзины = $58.29"):
        expected_total = "Total: $58.29"
        assert total_text == expected_total, f"Ожидалось '{
            expected_total}', но получили '{total_text}'"
