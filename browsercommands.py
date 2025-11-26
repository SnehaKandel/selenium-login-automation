from selenium import webdriver
from selenium.webdriver.common.by import By  
import time

# Use Chrome() with capital C
browser = webdriver.Chrome()
browser.get("https://opensource-demo.orangehrmlive.com/")
browser.maximize_window()

time.sleep(30)
browser.forward()
time.sleep(10)
browser.back()
time.sleep(10)
browser.refresh()
time.sleep(10)
browser.close()