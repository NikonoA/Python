from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, browser):
        self._browser = browser

    def checkout(self):
        self._browser.find_element(By.CSS_SELECTOR, "button#checkout").click()
