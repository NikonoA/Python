from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# open
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

sleep(2)

# click
button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

print("ok")
