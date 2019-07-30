"""
Комплексные решения (заказ 5 товаров из раздела комплексных решений) любым способом (самовывоз/доставка)
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from StandardOrder import StandardOrder


class ComplexSolution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=30)
        self.driver.set_page_load_timeout(time_to_wait=30)

    def test_order4(self):
        driver = self.driver
        driver.get("https://shop.saint-gobain.ru/")
        driver.find_element(By.XPATH, "//h3[@id='ui-id-7']").click()
        driver.find_elements(By.XPATH, "//a[contains(text(),'Внутренняя облицовка стен влажных помещений')]")[1].click()
        driver.find_element(By.XPATH, "//button[@class='btn-buy']").click()
        driver.find_element(By.XPATH, "//input[@id='edit-checkout']").click()
        driver.find_element(By.ID, "edit-customer-profile-shipping-string-address") \
            .send_keys("Россия, Москва, улица Большая Якиманка, 22к3")
        driver.find_element(By.XPATH, "//div[@class='controls']//input[2]").click()
        StandardOrder.test_user_info(self, driver)
        driver.find_element(By.ID, "edit-continue").click()
        driver.find_elements(By.CLASS_NAME, "fake-radio").pop().click()
        driver.find_element(By.XPATH, "//div[@class='controls']//input[1]").click()
        assert driver.find_element(By.XPATH, "//div[@class='order-complete']").is_displayed()
        assert driver.find_element(By.XPATH, "//div[@class='b-total']//div[@class='top']").is_displayed()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()