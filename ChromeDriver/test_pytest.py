import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
text = "Congratulations! You have successfully registered!"

class TesClassName(unittest.TestCase):
    def test_something(self):

        browser.get(link1)
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys("Ivan")
        last_name = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']").send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys("ivan.petrov@mail.ru")
        phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']").send_keys("89221112222")
        address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']").send_keys("Russia")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
        text2 = browser.find_element(By.TAG_NAME, "h1").text
        assert (text == text2)
        time.sleep(3)
        browser.quit()

    def test_something2(self):

        browser.get(link2)
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys("Ivan")
        last_name = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']").send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys("ivan.petrov@mail.ru")
        phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']").send_keys("89221112222")
        address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']").send_keys("Russia")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
        text2 = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(text == text2)
        time.sleep(5)
        browser.quit()

if __name__ == '__main__':
    unittest.main()
