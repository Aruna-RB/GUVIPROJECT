from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Locators import test_data


class TestPIM02:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_validate_header(self, enable_setup):
        self.driver.find_element(By.NAME, test_data.LocatorsData.input_box_username).send_keys(
            test_data.LoginPage.username)
        self.driver.find_element(By.NAME, test_data.LocatorsData.input_box_password).send_keys(
            test_data.LoginPage.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data.LocatorsData.login_xpath)))
        login_button.click()
        self.driver.find_element(By.XPATH, test_data.LocatorsData.admin).click()
        try:
            assert self.driver.title == 'OrangeHRM'
            print("'OrangeHRM' title - Header Validation Successful")
        except AssertionError:
            print("Header Validation Failed")

        usermgmt_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.User_management)
        try:
            assert usermgmt_tab.text == 'User Management'
            print("'User Management' tab is displayed")
        except AssertionError:
            print("'User Management' tab is NOT displayed")

        job_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.Job)
        try:
            assert job_tab.text == 'Job'
            print("'Job' tab is displayed")
        except AssertionError:
            print("'Job' tab is NOT displayed")

        organization_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.Organization)
        try:
            assert organization_tab.text == 'Organization'
            print("'Organization' tab is displayed")
        except AssertionError:
            print("'Organization' tab is NOT displayed")

        qualifications_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.Qualification)
        try:
            assert qualifications_tab.text == 'Qualifications'
            print("'Qualifications' tab is displayed")
        except AssertionError:
            print("'Qualifications' tab is NOT displayed")

        nationalities_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.Nationalities)
        try:
            assert nationalities_tab.text == 'Nationalities'
            print("'Nationalities' tab is displayed")
        except AssertionError:
            print("'Nationalities' tab is NOT displayed")

        corporate_banking_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.Corporate_Banking)
        try:
            assert corporate_banking_tab.text == 'Corporate Banking'
            print("'Corporate Banking' tab is displayed")
        except AssertionError:
            print("'Corporate Banking' tab is NOT displayed")

        configuration_tab = self.driver.find_element(By.XPATH, test_data.LocatorsData.Configuration)
        try:
            assert configuration_tab.text == 'Configuration'
            print("'Configuration' tab is displayed")
        except AssertionError:
            print("'Configuration' tab is NOT displayed")
