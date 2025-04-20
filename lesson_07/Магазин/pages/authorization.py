from selenium.webdriver.common.by import By


class Auth:

    def __init__(self, browser):
        self._browser = browser
        self._browser.get("https://www.saucedemo.com/")

    def login(self, data):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#user-name").send_keys(data)

    def password(self, term):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#password").send_keys(term)
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#login-button").click()
