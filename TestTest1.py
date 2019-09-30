import unittest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))


class TestTest1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/Сергей/PycharmProjects/testselenium/chromedriver.exe')
        self.driver.implicitly_wait(time_to_wait=30)
        self.driver.set_page_load_timeout(time_to_wait=30)

    def test_some_function(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/file_input.html")
        name_element = driver.find_element_by_xpath("//input[@placeholder='Enter first name']")
        name_element.send_keys('Jon')

        submit = driver.find_element_by_xpath("//button[@type='submit']")

        surname_element = driver.find_element_by_xpath("//input[@placeholder='Enter last name']")
        surname_element.send_keys('Jonson')
        email_element = driver.find_element_by_xpath("//input[@placeholder='Enter email']")
        email_element.send_keys('1@meil.com')

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'textfile_1.txt')
        file_element = driver.find_element_by_id('file')
        file_element.send_keys(file_path)
        submit.click()
        assert driver.get_screenshot_as_png()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
