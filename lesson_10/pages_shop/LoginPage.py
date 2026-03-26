from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class LoginPage:
    def __init__(self, driver: WebDriverWait) -> None:
        """
        Конструктор класса CartPage.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ввод данных пользователя {username} и {password}, нажатие кнопки Login")
    def login(self, username: str, password: str) -> None:
        """
        Ввод имени пользователя и пароля, нажатие кнопки Login.
        :param user-name: str - имя пользователяю
        :param password: str - пароль пользователя"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
