
from selenium import webdriver
import time

username = "admin"
password = "admin"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth")

time.sleep(5)
