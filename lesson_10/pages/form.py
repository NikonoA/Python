from selenium.webdriver.common.by import By


class Form:
    """Заполнение формы для заказа товаров"""

    def __init__(self, browser: str) -> None:
        self._browser = browser

    def form_name(self, data: str) -> str:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#first-name").send_keys(data)

    def form_last_name(self, data: str) -> str:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#last-name").send_keys(data)

    def form_adress(self, data: str) -> str:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#postal-code").send_keys(data)

    def next(self) -> None:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#continue").click()

    def count(self):
        total = self._browser.find_element(By.CSS_SELECTOR,
                                           "div.summary_total_label").text
        return total
