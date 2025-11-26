import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# --------------------------
# Read CSV file
# --------------------------
csv_file = 'testdata.csv'
test_data = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

print("Loaded Test Data:", test_data)


# --------------------------
# Run Test for Each Row
# --------------------------
for data in test_data:

    print(f"\nRunning test for: {data}")

    # Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open website
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Enter username
    driver.find_element(By.ID, "user-name").send_keys(data['username'])

    # Enter password
    driver.find_element(By.ID, "password").send_keys(data['password'])

    # Click login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # Close browser
    driver.quit()
