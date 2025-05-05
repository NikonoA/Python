from selenium.webdriver.common.by import By
import allure

link = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


class Delay:
    """
    В классе указаны действия с окошком ввода:
    очистка и ввод значения (числового)
    """

    def __init__(self, browser: str) -> None:
        self._browser = browser
        self._browser.get(link)

    @allure.step("Delay. Проверка ожидания")
    def form_delay(self, term: int) -> int:
        self._browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)
