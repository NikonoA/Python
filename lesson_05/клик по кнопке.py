from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# open
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(2)

# click 5 times
button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()
button.click()
button.click()
button.click()
button.click()

sleep(2)

# find and count button "Delete"
delete = driver.find_elements(By.CSS_SELECTOR, ".added-manually")

print(len(delete))
