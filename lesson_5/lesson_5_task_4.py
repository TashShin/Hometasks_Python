from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By. CSS_SELECTOR, "input#username")
username_input.send_keys("tomsmith")
password_input = driver.find_element(By. CSS_SELECTOR, "input#password")
password_input.send_keys("SuperSecretPassword!")
target_button = driver.find_element(By.CLASS_NAME, "radius").click()

flash_element = driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success")
print(flash_element.text)

sleep(5)

driver.quit()
