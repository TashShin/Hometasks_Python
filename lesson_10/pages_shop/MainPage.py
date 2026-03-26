from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class MainPage:
    def __init__(self, driver: WebDriverWait) -> None:
        """
        Конструктор класса CartPage.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товаров в корзину по ID - {item_id}")
    def add_to_cart(self, item_id: str) -> None:
        selector = f"#add-to-cart-{item_id}"
        self.driver.find_element(By.CSS_SELECTOR, selector).click()

    @allure.step("Переход в корзину через нажатие иконки")
    def go_to_cart(self) -> None:
        """
        Переход в корзину через нажатие иконки.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
