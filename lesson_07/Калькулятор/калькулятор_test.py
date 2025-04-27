from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from steps.form_delay import Delay
from steps.buttons import Buttons

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
to_be = 15


def test_calculator():

    delay = Delay(driver)
    delay.form_delay("45")

    buttons = Buttons(driver)
    buttons.enter_numbers()
    wait1 = WebDriverWait(driver, 46)
    wait1.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15")
            )
    as_it = buttons.count()
    assert as_it == to_be
