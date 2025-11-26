from selenium import webdriver
import time
from selenium.webdriver.common.by import By  

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")


iframe=browser.find_element(By.ID , "" )
browser.switch_to.frame(iframe)

text_editor=browser.find_element(By.ID , "")
text_editor.clear()
text_editor.send_keys("iframe example")
