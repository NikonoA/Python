from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.authorization import Auth
from pages.main_page import Main
from pages.cart import Cart
from pages.form import Form
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
to_be = "Total: $58.29"


def test_shopping():

    auth = Auth(driver)
    auth.login("standard_user")
    auth.password("secret_sauce")
    main = Main(driver)
    main.goods()
    wait1 = WebDriverWait(driver, 15)
    wait1.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.title"), "Your Cart")
            )
    cart = Cart(driver)
    cart.checkout()
    form = Form(driver)
    form.form_name("Aliona")
    form.form_last_name("Nikonorova")
    form.form_adress("111111")
    form.next()
    as_it = form.count()
    assert as_it == to_be
