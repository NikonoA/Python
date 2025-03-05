from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

tag = "input"
search = driver.find_element(By.TAG_NAME, tag)

search.send_keys("1000")

sleep(2)

search.clear()

sleep(1)

search.send_keys("999")
