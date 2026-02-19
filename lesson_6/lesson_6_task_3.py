from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

fourth_pic = WebDriverWait(driver, 20)
fourth_pic.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

third_pic = driver.find_element(By.CSS_SELECTOR, "#award")

att = third_pic.get_attribute("src")

print(att)

driver.quit()
