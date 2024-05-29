import time
import unittest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogout(unittest.TestCase):

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
    def test_logout_valid(self):
        driver = self.driver

        driver.get('https://www.demoblaze.com/index.html')
        driver.find_element(By.ID, "login2").click()
        time.sleep(1)
        driver.find_element(By.ID, "loginusername").send_keys("MuniRTR")
        time.sleep(1)
        driver.find_element(By.ID, "loginpassword").send_keys("Test123456")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@onClick='logIn()']").click()
        print("Login Successfull")
        time.sleep(3)
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\LogoutPage.png")
        time.sleep(5)
        driver.find_element(By.ID, "logout2").click()
        print("successfully logged out from the home page")
