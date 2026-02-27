from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    goods_to_buy = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
        ]

    for good_id in goods_to_buy:
        button_selector = f"#add-to-cart-{good_id}"
        driver.find_element(By.CSS_SELECTOR, button_selector).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Natalya")
    driver.find_element(By.ID, "last-name").send_keys("Evdokimova")
    driver.find_element(By.ID, "postal-code").send_keys("413107")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10)
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_cost.text

    driver.quit()

    assert total_text == "Total: $58.29", f"Expected Total: $58.29 received '{
        total_text}'"
