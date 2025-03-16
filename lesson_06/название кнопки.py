from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://uitestingplayground.com/textinput")

button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

button.send_keys("SkyPro")

button1 = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

button1.click()

newButton = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(newButton)

driver.quit()
