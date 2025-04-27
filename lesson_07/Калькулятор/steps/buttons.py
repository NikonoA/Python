from selenium.webdriver.common.by import By


class Buttons:

    def __init__(self, browser):
        self._browser = browser

    def enter_numbers(self):
        self._browser.find_element(By.XPATH, '//span[text()="7"]').click()
        self._browser.find_element(By.XPATH, '//span[text()="+"]').click()
        self._browser.find_element(By.XPATH, '//span[text()="8"]').click()
        self._browser.find_element(By.XPATH, '//span[text()="="]').click()

    def count(self):
        txt = self._browser.find_element(By.CSS_SELECTOR, ".screen").text
        return int(txt)
