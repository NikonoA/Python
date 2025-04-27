from selenium.webdriver.common.by import By


class Form:
    def __init__(self, browser):
        self._browser = browser

    def form_name(self, data):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#first-name").send_keys(data)

    def form_last_name(self, data):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#last-name").send_keys(data)

    def form_adress(self, data):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#postal-code").send_keys(data)

    def next(self):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "input#continue").click()

    def count(self):
        total = self._browser.find_element(By.CSS_SELECTOR,
                                           "div.summary_total_label").text
        return total
