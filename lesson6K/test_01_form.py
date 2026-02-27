from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "D:/Testing/Учеба/edgedriver/msedgedriver.exe"


def test_page():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 5)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.visibility_of_element_located((By.ID, "zip-code")))
    zip_code_result = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_result.get_attribute(
        "class"), "Zip code не подсвечен красным"

    fields_success = ["first-name", "last-name", "address", "e-mail", "phone",
                      "city", "country", "job-position", "company"]
    for field_id in fields_success:
        field_element = driver.find_element(By.ID, field_id)
        assert "alert-success" in field_element.get_attribute(
            "class"), f"Поле {field_id} не подсвечено зеленым!"

    driver.quit()
