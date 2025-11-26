from selenium import webdriver
import time
from selenium.webdriver.common.by import By  
import requests  

browser = webdriver.Chrome()
browser.get("https://www.daraz.com.np/")  
time.sleep(2)

images = browser.find_elements(By.TAG_NAME, "img")
print(f"Total images: {len(images)}")


for image in images:
    src = image.get_attribute('src')
response = requests.get(src)

if response.status_code != 200:

print(f"Broken Image found: {src}")



browser.quit()