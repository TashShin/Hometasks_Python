from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages_shop.LoginPage import LoginPage
from pages_shop.MainPage import MainPage
from pages_shop.CartPage import CartPage
from pages_shop.CheckPage import CheckPage


def test_shop_with_page_objects():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    check_page = CheckPage(driver)

    login_page.login("standard_user", "secret_sauce")

    goods_to_buy = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]
    for good_id in goods_to_buy:
        main_page.add_to_cart(good_id)

    main_page.go_to_cart()
    cart_page.checkout()

    check_page.fill_form("Natalya", "Evdokimova", "412365")

    total_text = check_page.get_total_price()

    driver.quit()

    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Ожидалось '{
        expected_total}', но получили '{total_text}'"
