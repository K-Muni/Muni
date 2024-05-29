import time
import unittest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCart(unittest.TestCase):

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
    def test_add_last_product_to_cart(self):
        driver = self.driver
        driver.get('https://www.demoblaze.com/index.html')
        driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        driver.find_element(By.ID, "loginusername").send_keys("MuniRTR")
        time.sleep(2)
        driver.find_element(By.ID, "loginpassword").send_keys("Test123456")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@onClick='logIn()']").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\NextPage.png")

        driver.find_element(By.ID, 'next2').click()
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\EndPage.png")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "MacBook Pro").click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Add to cart").click()
        print("product added to cart successfully")
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\CartPage.png")
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.accept()
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\Alert.png")

        time.sleep(2)
        driver.find_element(By.ID,"cartur").click()
        print("Successfully check the items added to the cart.")


if __name__ == '__main__':
    unittest.main()
