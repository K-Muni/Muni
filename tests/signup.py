import time
import unittest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class TestSignup(unittest.TestCase):

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
    def test_signup_valid(self):
        driver = self.driver
        driver.get('https://www.demoblaze.com/index.html')
        driver.find_element(By.ID, "signin2").click()
        time.sleep(5)
        driver.find_element(By.ID, "sign-username").send_keys("MuniRTR")
        time.sleep(5)
        driver.find_element(By.ID, "sign-password").send_keys("Test123456")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@onClick='register()']").click()
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.accept()
        print("Successfully registered")
        # Add assertions to verify signup success

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signup_invalid(self):
        driver = self.driver
        driver.get('https://www.demoblaze.com/index.html')
        time.sleep(5)

        driver.find_element(By.ID, "signin2").click()
        time.sleep(5)
        driver.find_element(By.ID, "sign-username").send_keys("")
        time.sleep(5)
        driver.find_element(By.ID, "sign-password").send_keys("Test123456")
        time.sleep(3)
        driver.save_screenshot("C:\\Users\\rockt\\Downloads\\E-Commmerce_Project1\\Screenshots\\Signup.png")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@onClick='register()']").click()

        time.sleep(5)
        alert = driver.switch_to.alert
        alert.accept()

        print("Please fill out Username and Password.")
        # Add assertions to verify signup failure


if __name__ == '__main__':
    unittest.main()
