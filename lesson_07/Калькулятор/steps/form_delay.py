from selenium.webdriver.common.by import By

link = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


class Delay:

    def __init__(self, browser):
        self._browser = browser
        self._browser.get(link)

    def form_delay(self, term):
        self._browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)
