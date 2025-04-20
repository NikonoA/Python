import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR,
                        "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR,
                        "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR,
                        "#login-button").click()

    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR,
                        "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR,
                        "button#checkout").click()

    driver.find_element(By.CSS_SELECTOR,
                        "input#first-name").send_keys("Aliona")
    driver.find_element(By.CSS_SELECTOR,
                        "input#last-name").send_keys("Nikonorova")
    driver.find_element(By.CSS_SELECTOR,
                        "input#postal-code").send_keys("111111")
    driver.find_element(By.CSS_SELECTOR,
                        "input#continue").click()

    total = driver.find_element(By.CSS_SELECTOR,
                                "div.summary_total_label").text

    print(total)

    driver.quit()

    assert total == "Total: $58.29"
