from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from page_calc.CalcPage import CalcPage


def test_slow_calculator_pom():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    calc_page = CalcPage(driver)

    calc_page.set_delay(45)
    buttons = ["7", "+", "8", "="]
    for btn in buttons:
        calc_page.click_button(btn)

    result = calc_page.get_result("15", 50)

    driver.quit()

    assert result == "15", f"Ожидалось 15, но на экране отобразилось: {result}"
