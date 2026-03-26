from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure

from page_calc.CalcPage import CalcPage


@allure.title("Тестирование калькулятора")
@allure.description("Тестирование калькулятора с отсрочкой получаемого результата")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator_pom():
    with allure.step("Открытие браузера и переход на сайт калькулятора"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()

    calc_page = CalcPage(driver)

    with allure.step("Очистка поля времени и установка заданного ожидания"):
        calc_page.set_delay(45)

    with allure.step("Нажатие кнопок калькулятора"):
        buttons = ["7", "+", "8", "="]
        for btn in buttons:
            calc_page.click_button(btn)

    with allure.step("Получение результата"):
        result = calc_page.get_result("15", 50)

    with allure.step("Закрытие браузера"):
        driver.quit()

    with allure.step("Проверка результата"):
        assert result == "15", f"Ожидалось 15, но на экране отобразилось: {result}"
