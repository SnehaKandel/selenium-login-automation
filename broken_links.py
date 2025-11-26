from selenium import webdriver
import time
from selenium.webdriver.common.by import By  
import requests  

browser = webdriver.Chrome()
browser.maximize_window() 
browser.get("https://www.daraz.com.np/?spm=a2a0e.pdp.header.dhome.6f063afbkSjw0D#?")  

time.sleep(2)  #page load


all_links = browser.find_elements(By.TAG_NAME, "a")
print(f"Total links found: {len(all_links)}")  #counts the total no of links 


for link in all_links:
    href = link.get_attribute('href')
    

response = requests.get(href)
if response.status_code >= 400:  
 print(f"Broken link: {href} (Status code: {response.status_code})")

time.sleep(10)
browser.quit()