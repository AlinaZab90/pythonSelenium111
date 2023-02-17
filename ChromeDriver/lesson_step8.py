from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.XPATH, "//input")
    options = string.ascii_lowercase
    for element in elements:
        random_world = ''.join(random.choice(options) for _ in range(5))
        element.send_keys(random_world)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

