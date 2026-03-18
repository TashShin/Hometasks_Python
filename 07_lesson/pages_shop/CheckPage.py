from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        # Используем явное ожидание для получения цены
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
