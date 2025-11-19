from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By
import time

# Use Chrome() with capital C
browser = webdriver.Chrome()
browser.maximize_window()

username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"
browser.get(login_url)

# small delay to ensure page loads completely
time.sleep(2)

# Find elements
username_field = browser.find_element(By.ID, "user-name")
password_field = browser.find_element(By.ID, "password")
login_button = browser.find_element(By.ID, "login-button")

# Perform login
username_field.send_keys(username)
password_field.send_keys(password)

# Check if login button is enabled and click
assert not login_button.get_attribute("disabled"), "Login button is disabled"
login_button.click()

# Wait for page to load after login
time.sleep(3)

# Verify successful login
success_element = browser.find_element(By.CSS_SELECTOR, ".title") #copy relative css selector using selectorshub browser extention
assert success_element.text == "Products"

print("Login successful! Navigated to Products page.")

#  Wait to see the result
time.sleep(5)
browser.quit()