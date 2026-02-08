from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
wait = WebDriverWait(driver, 5)


target_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click
print("Кнопка нажата")

sleep(5)
