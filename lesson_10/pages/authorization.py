from selenium.webdriver.common.by import By
import allure


class Auth:
    """
    Работа со страницей авторизации:
    ввод логина, пароля и нажатие кнопки "Войти"
    """

    def __init__(self, browser: str) -> None:
        self._browser = browser
        self._browser.get("http://www.saucedemo.com/")

    @allure.step("Auth. Ввод логина")
    def login(self, data: str) -> None:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#user-name").send_keys(data)

    @allure.step("Auth. Ввод пароля")
    def password(self, term: str) -> None:
        self._browser.find_element(By.CSS_SELECTOR,
                                   "#password").send_keys(term)
        pas = self._browser.find_element(By.CSS_SELECTOR,
                                         "#login-button")
        pas.click()
