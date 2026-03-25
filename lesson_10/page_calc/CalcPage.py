from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:

    def __init__(self, driver: WebDriverWait):
        """
        Конструктор класса CalcPage.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Очистка поля времени и установка заданного ожидания в {seconds}")
    def set_delay(self, seconds: int) -> int:
        """
        Очищает поле времени задержки и устанавливает заданное время.
        :param seconds: int - время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажатие кнопки {buttons}")
    def click_button(self, buttons: list[str]) -> list[str]:
        """
        Нажимает на кнопку калькулятора.
        :param buttons: list[str] - список текстов на нажимаемых кнопках.
        """
        xpath = f"//span[text()='{buttons}']"
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Получение ожидаемого результата {expected_value} при заданной отсрочке {timeout}")
    def get_result(self, expected_value: str, timeout: int) -> str:
        """
        Возвращает текущий результат с экрана калькулятора.
        :param expected_value: str - ожидаемый результат.
        :param timeout: int - время задержки в секундах"""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), expected_value)
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
