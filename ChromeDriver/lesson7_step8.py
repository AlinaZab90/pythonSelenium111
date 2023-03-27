import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link1 = "http://suninjuly.github.io/registration1.html"
    #link2 = "http://suninjuly.github.io/registration2.html"
    #тест проходит по ссылке1 и падает на ссылке2

    browser = webdriver.Chrome()
    browser.get(link1)

    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']").send_keys("Ivanov")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys("ivan.petrov@mail.ru")
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']").send_keys("89221112222")
    address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']").send_keys("Russia")

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    time.sleep(5)
    browser.quit()
