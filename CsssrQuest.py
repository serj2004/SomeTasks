"""
Проверка ссылки «Софт для быстрого создания скриншотов» (должна вести сюда http://monosnap.com/ )
"""


from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class CsssrQuest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)

    def test_link_check(self):
        driver = self.driver
        driver.get("http://csssr.github.io/qa-engineer/")
        driver.find_element(By.XPATH, "//a[text()='НАХОДИТЬ НЕСОВЕРШЕНСТВА']").click()
        a = driver.window_handles[0]
        driver.find_element(By.XPATH, "//a[text()='Софт для быстрого создания скриншотов']").click()
        driver.implicitly_wait(6000)
        b = driver.window_handles[1]
        driver.switch_to.window(b)

        if  "Monosnap" in self.driver.title:
            print("SUCCESS!")
        else:
            print("OOOPS..")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()