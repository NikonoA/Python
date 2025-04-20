from selenium.webdriver.common.by import By


class Main:
    def __init__(self, browser):
        self._browser = browser

    def goods(self):
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#add-to-cart-sauce-labs-backpack").click()
        sh = self._browser.find_element(By.CSS_SELECTOR,
                                        "#add-to-cart-sauce-labs-bolt-t-shirt")
        sh.click()
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#add-to-cart-sauce-labs-onesie").click()
        self._browser.find_element(By.CSS_SELECTOR,
                                   "a.shopping_cart_link").click()
