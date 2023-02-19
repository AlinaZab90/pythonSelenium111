from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.XPATH, "//*[@name='firstname']")
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.XPATH, "//*[@name='lastname']")
    lastname.send_keys("Petrov")
    email = browser.find_element(By.XPATH, "//*[@name='email']")
    email.send_keys("abcdef@mail.ru")

    file = browser.find_element(By.ID, "file")
    directory = os.path.abspath(os.path.dirname(__file__))
    #получаем путь к директории текущего исполняемого файла

    file_path = os.path.join(directory, 'Selenium.txt')
    #добавляем к этому пути имя файла
    print(file_path) #при необходимости печатаем

    file.send_keys(file_path)
    #добавляем файл

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
finally:
    time.sleep(5)
    browser.quit()
