from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from locators import test_data_pim_02


class TestLogin1:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def valid_login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, test_data_pim_02.Locators.input_box_username).send_keys(
            test_data_pim_02.LoginPage.username)
        self.driver.find_element(By.NAME, test_data_pim_02.Locators.input_box_password).send_keys(
            test_data_pim_02.LoginPage.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_02.Locators.login_xpath)))
        login_button.click()

    def navigate_to_pim(self):
        self.driver.find_element(By.XPATH, test_data_pim_02.AccessPim.pim_tab).click()
        self.driver.find_element(By.XPATH, test_data_pim_02.AccessPim.input_box_employeeName).send_keys(
            test_data_pim_02.ModifyDetails.employeeName)
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_02.AccessPim.search)))
        search_box.click()

    def modify_details(self):
        self.driver.find_element(By.XPATH, test_data_pim_02.UpdateInfo.edit).click()
        self.driver.find_element(By.NAME, test_data_pim_02.UpdateInfo.middlename_input_box).send_keys(
            Keys.CONTROL, test_data_pim_02.ModifyDetails.middleName)
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_02.UpdateInfo.save_button)))
        save.click()


TestLogin1().enable_setup()
TestLogin1().valid_login()
TestLogin1().navigate_to_pim()
TestLogin1().modify_details()
