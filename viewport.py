from selenium import webdriver
from selenium.webdriver.common.by import By  
import time


viewports = [(500, 600), (700, 800), (800, 700), (400, 200)]  

browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")

try:
    
    for width, height in viewports:
        browser.set_window_size(width, height)
        time.sleep(2)  #to see each resize
        
finally:
    browser.close()  # or browser.quit()

