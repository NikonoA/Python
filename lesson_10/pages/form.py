from selenium.webdriver.common.by import By
import allure


class Form:
    """Заполнение формы для заказа товаров"""

    def __init__(self, browser: str) -> None:
        self._browser = browser

    @allure.step("Form. Ввести имя")
    def form_name(self, data: str) -> str:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#first-name").send_keys(data)

    @allure.step("Form. Ввести фамилию")
    def form_last_name(self, data: str) -> str:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#last-name").send_keys(data)

    @allure.step("Form. Ввести адрес")
    def form_adress(self, data: str) -> str:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#postal-code").send_keys(data)

    @allure.step("Form. Переход на новую страницу")
    def next(self) -> None:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#continue").click()

    @allure.step("Form. Подсчёт суммы")
    def count(self):
        total = self._browser.find_element(By.CSS_SELECTOR,
                                           "div.summary_total_label").text
        return total
