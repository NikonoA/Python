from selenium.webdriver.common.by import By


class Cart:
    """Работа со страницей корзины (заказ товаров)"""

    def __init__(self, browser: str) -> None:
        self._browser = browser

    def checkout(self) -> None:
        self._browser.find_element(By.CSS_SELECTOR, "button#checkout").click()
