from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from Pages import loginpage


class TestLogin1:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def forgot_password(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CLASS_NAME, loginpage.Locators.forgot_password).click()
        self.driver.find_element(By.NAME, loginpage.Locators.username_textbox).send_keys(loginpage.Data.username)
        self.driver.find_element(By.XPATH, loginpage.Locators.reset_password).click()
        verify = driver.find_element(By.XPATH, loginpage.Locators.verification)
        assert verify.text == "A reset password link has been sent to you via email."


TestLogin1().enable_setup()
TestLogin1().forgot_password()
