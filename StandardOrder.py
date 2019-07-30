"""
Стандартный заказ с расчетом стоимости доставки
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class StandardOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=30)
        self.driver.set_page_load_timeout(time_to_wait=30)

    def test_order2(self):
        driver = self.driver
        driver.get("https://shop.saint-gobain.ru/")
        driver.find_element(By.XPATH, "//div[@id='ui-id-2']//ul//li[1]").click()
        driver.find_element(By.XPATH, "//div[contains(@class,'view-content container')]//div[1]//div[6]//a[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[1]/div[3]"
                                      "/span[1]/a[1]").click()
        driver.find_element(By.XPATH, "//span[@title='Добавить товар в корзину']").click()
        driver.find_element(By.XPATH, "//input[@id='edit-checkout']").click()
        assert driver.find_element(By.XPATH, "//div[contains(text(),'доставка')]").is_displayed()
        driver.find_element(By.ID, "edit-customer-profile-shipping-string-address").send_keys \
            ("Россия, Москва, улица Большая Якиманка, 22к3")
        driver.find_element(By.XPATH, "//div[@class='controls']//input[2]").click()
        assert driver.find_element(By.XPATH, "//div[contains(text(),'Доставка')]").is_displayed()
        self.test_user_info(driver)
        driver.find_element(By.ID, "edit-continue").click()
        driver.find_elements(By.CLASS_NAME, "fake-radio").pop().click()
        driver.find_element(By.XPATH, "//div[@class='controls']//input[1]").click()
        assert driver.find_element(By.XPATH, "//div[@class='order-complete']").is_displayed()
        assert driver.find_element(By.XPATH, "//div[@class='b-total']//div[@class='top']").is_displayed()

    def test_user_info(self, driver):
        driver.find_element(By.ID, "edit-customer-profile-billing-field-customer-recepient-email-und-0-value") \
            .send_keys("test@mmm.com")
        driver.find_element(By.ID, "edit-customer-profile-billing-field-user-first-name-und-0-value").send_keys("Иван")
        driver.find_element(By.ID, "edit-customer-profile-billing-field-user-last-name-und-0-value").send_keys("Иванов")
        driver.find_element(By.ID, "edit-customer-profile-billing-field-user-phone-und-0-value").send_keys("1234567890")
        driver.find_element(By.ID, "edit-customer-profile-billing-agreement").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()