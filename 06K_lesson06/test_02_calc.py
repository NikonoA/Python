import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".display-6"), "Slow calculator")
        )

    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    wait1 = WebDriverWait(driver, 46)
    wait1.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15")
            )

    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
