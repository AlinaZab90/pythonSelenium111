from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element(By.XPATH, "//img[@valuex]")
    x = img.get_attribute("valuex")

    y = calc(x)

    inputs = browser.find_element(By.CSS_SELECTOR, "#answer")
    inputs.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
