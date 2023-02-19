from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    x = number1.text
    number2 = browser.find_element(By.XPATH, "//span[@id='num2']")
    y = number2.text
    summ = str(int(x) + int(y))

    select = Select(browser.find_element(By.XPATH, "//select"))
    select.select_by_value(summ)

    browser.find_element(By.XPATH, "//button").click()

finally:
    time.sleep(10)
    browser.quit()