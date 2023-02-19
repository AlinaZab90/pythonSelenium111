import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, " #input_value")
    x = x_element.text
    y = calc(x)

    inputs = browser.find_element(By.CSS_SELECTOR, " #answer")
    inputs.send_keys(y)

    options1 = browser.find_element(By.CSS_SELECTOR, " [for ='robotCheckbox']").click()
    options2 = browser.find_element(By.CSS_SELECTOR, " [for ='robotsRule']").click()

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
