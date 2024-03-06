from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Pages import loginpage


class TestForgot1:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_forgot_password(self, enable_setup):
        self.driver.find_element(By.CLASS_NAME, loginpage.Locators.forgot_password).click()
        self.driver.find_element(By.NAME, loginpage.Locators.username_textbox).send_keys(loginpage.Data.username)
        self.driver.find_element(By.XPATH, loginpage.Locators.reset_password).click()
        # verify = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, loginpage.Locators.verification)))
        verify = self.driver.find_element(By.XPATH, loginpage.Locators.verification)
        assert verify.text == "A reset password link has been sent to you via email."
