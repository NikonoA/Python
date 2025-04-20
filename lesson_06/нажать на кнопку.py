from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://uitestingplayground.com/ajax")

wait_button = WebDriverWait(driver, 20)

button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")

wait_button.until(
    EC.element_to_be_clickable((button)))

button.click()

wait = WebDriverWait(driver, 20, 0.1)

wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "p.bg-success"),
        "Data loaded with AJAX get request.")
)

txt = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()
