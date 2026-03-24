from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.TAG_NAME, "input")
search_input.send_keys("Sky")
search_input.clear()
search_input.send_keys("Pro")

print("Успешно выполнено")

driver.quit()
