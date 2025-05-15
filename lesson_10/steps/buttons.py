from selenium.webdriver.common.by import By
import allure


class Buttons:
    """
    В классе указаны действия с кнопками: цифры и Enter
    """
    def __init__(self, browser: str) -> None:
        self._browser = browser

    @allure.step("Buttons. Проверка кнопок калькулятора")
    def enter_numbers(self) -> None:
        with allure.step("Проверка цифры 7"):
            self._browser.find_element(By.XPATH, '//span[text()="7"]').click()
        with allure.step("Проверка знака +"):
            self._browser.find_element(By.XPATH, '//span[text()="+"]').click()
        with allure.step("Проверка цифры 8"):
            self._browser.find_element(By.XPATH, '//span[text()="8"]').click()
        with allure.step("Проверка знака ="):
            self._browser.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Buttons. Проверка счёта")
    def count(self) -> int:
        txt = self._browser.find_element(By.CSS_SELECTOR, ".screen").text
        return int(txt)
