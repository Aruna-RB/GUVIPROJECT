from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from Locators import test_data_pim_03


class TestPIM03:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def valid_login(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, test_data_pim_03.Locators.input_box_username).send_keys(
            test_data_pim_03.LoginPage.username)
        self.driver.find_element(By.NAME, test_data_pim_03.Locators.input_box_password).send_keys(
            test_data_pim_03.LoginPage.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_03.Locators.login_xpath)))
        login_button.click()

    def navigate_to_pim(self):
        self.driver.find_element(By.XPATH, test_data_pim_03.Locators.pim_tab).click()
        self.driver.find_element(By.XPATH, test_data_pim_03.Locators.input_box_employeeName).send_keys(
            test_data_pim_03.LoginData.employeeName)
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_03.Locators.search)))
        search_box.click()

    def delete_details(self):
        self.driver.find_element(By.XPATH, test_data_pim_03.Locators.delete).click()
        delete_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_03.Locators.delete_button)))
        delete_tab.click()


TestPIM03().booting_function()
TestPIM03().valid_login()
TestPIM03().navigate_to_pim()
TestPIM03().delete_details()
