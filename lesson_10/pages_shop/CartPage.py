from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CartPage:
    def __init__(self, driver: WebDriverWait):
        """
        Конструктор класса CartPage.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие кнопки Checkout для перехода к оформлению заказа")
    def checkout(self):
        """
        Нажатие кнопки Checkout для перехода к оформлению заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()
