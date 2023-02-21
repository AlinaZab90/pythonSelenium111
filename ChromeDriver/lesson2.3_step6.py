from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//*[@type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(3)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.XPATH, "//*[@type='submit']").click()

    alert = browser.switch_to.alert
    print(alert.text)


finally:
    time.sleep(3)
    browser.quit()
