from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, buttons):
        xpath = f"//span[text()='{buttons}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, expected_value, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), expected_value)
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
