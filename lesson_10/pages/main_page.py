from selenium.webdriver.common.by import By
import allure


class Main:
    """Главная страница, добавление товаров в корзину"""
    def __init__(self, browser: str) -> None:
        self._browser = browser

    @allure.step("Main. Добавление товаров")
    def goods(self) -> None:
        with allure.step("Добавить рюкзак"):
            self._browser.find_element(By.CSS_SELECTOR,
                                       "#add-to-cart-sauce-labs-backpack"
                                       "").click()
        with allure.step("Добавить футболку"):
            sh = self._browser.find_element(By.CSS_SELECTOR,
                                            "#add-to-cart-sauce-labs-bolt"
                                            "-t-shirt")
            sh.click()
        with allure.step("Добавить боди"):
            self._browser.find_element(By.CSS_SELECTOR,
                                       "#add-to-cart-sauce-labs-onesie"
                                       "").click()
        with allure.step("Переход в корзину"):
            self._browser.find_element(By.CSS_SELECTOR,
                                       "a.shopping_cart_link").click()
