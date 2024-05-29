import time
import unittest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProductBrowsing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        if hasattr(self, '_outcome') and not self._outcome.success:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_product(self):
        driver = self.driver
        driver.get('https://www.demoblaze.com/index.html')
        driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        driver.find_element(By.ID, "loginusername").send_keys("MuniRTR")
        time.sleep(2)
        driver.find_element(By.ID, "loginpassword").send_keys("Test123456")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@onClick='logIn()']").click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\Dashboard.png")
        if driver.find_element(By.ID, 'nava').is_displayed():
            print("products are  displayed")

        else:
            print("products are not displayed")
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\ProductList.png")
        # self.assertGreater(len(products), 0, 'products are displayed correctly on the homepage')
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "CATEGORIES").click()
        print("product categories can be navigated successfully.")



if __name__ == '__main__':
    unittest.main()
