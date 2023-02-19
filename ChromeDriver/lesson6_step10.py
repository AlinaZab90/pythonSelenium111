import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    options = string.ascii_lowercase

    elements_first = browser.find_elements(By.XPATH, "//label[contains(text(), '*')]")
    for element in elements_first:
        random_world = ''.join(random.choice(options) for _ in range(6))
        element.send_keys(random_world)

    #elements_second = browser.find_elements(By.CSS_SELECTOR, "second_block")
    #for element2 in elements_second:
        #random_world = ''.join(random.choice(options) for _ in range(8))
        #element2.send_keys(random_world)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(3)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(6)
    browser.quit()
