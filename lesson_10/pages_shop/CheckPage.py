from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckPage:
    def __init__(self, driver: WebDriverWait) -> None:
        """
        Конструктор класса CartPage.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Заполнение формы оформления заказа: Имя {first_name}, Фамилия {last_name}, Индекс {zip_code}")
    def fill_form(self, first_name, last_name, zip_code) -> None:
        """
        Заполнение формы оформления заказа: Имя, Фамилия, Индекс.
        :param first_name: str - имя покупателя.
        :param last_name: str - фамилия покупателя.
        :param zip_code: int - индекс покупателя.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой стоимости со страницы")
    def get_total_price(self) -> float:
        """
        Получение итоговой стоимости выбранных товаров.
        Используем явное ожидание для получения цены.
        """
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
