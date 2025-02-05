from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Enter credentials
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Wait for result and verify login success
time.sleep(2)
assert "You logged into a secure area!" in driver.page_source

# Close browser
driver.quit()
