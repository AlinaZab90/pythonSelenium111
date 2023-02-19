from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    inputs = browser.find_element(By.ID, "answer")
    inputs.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox").click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
