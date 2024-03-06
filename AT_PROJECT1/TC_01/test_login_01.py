from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import test_info_01
import pytest


class TestLogin1:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_valid_login(self, enable_setup):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.NAME, test_info_01.Data.input_box_username).send_keys(
                test_info_01.LoginPage.username)
            self.driver.find_element(By.NAME, test_info_01.Data.input_box_password).send_keys(
                test_info_01.LoginPage.password)
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, test_info_01.Data.login_xpath)))
            login_button.click()

        except NoSuchElementException as invalid_login:
            print(invalid_login)

        # finally:
        #     self.driver.quit()
        #     sleep(4)

# TestLogin1().test_valid_login()
# print("The user is logged in successfully")
