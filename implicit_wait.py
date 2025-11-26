from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements

driver.get("https://example.com")

# Selenium will wait up to 10 seconds if this element is not immediately present
element = driver.find_element_by_id("submit_button")
element.click()
