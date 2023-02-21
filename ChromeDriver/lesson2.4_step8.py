import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(By.ID, "book").click()

submit = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0]", submit)
x = browser.find_element(By.ID, "input_value").text
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
submit.click()
alert = browser.switch_to.alert
print(alert.text)
time.sleep(5)
browser.quit()
