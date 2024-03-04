import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Locators import test_data_pim_03


class TestPIM03:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_delete_info(self, enable_setup):
        self.driver.find_element(By.NAME, test_data_pim_03.LocatorData.input_box_username).send_keys(
            test_data_pim_03.LoginData.username)
        self.driver.find_element(By.NAME, test_data_pim_03.LocatorData.input_box_password).send_keys(
            test_data_pim_03.LoginData.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_03.LocatorData.login_xpath)))
        login_button.click()
        self.driver.find_element(By.XPATH, test_data_pim_03.LocatorData.pim_tab).click()
        self.driver.find_element(By.XPATH, test_data_pim_03.LocatorData.input_box_employeeName).send_keys(
            test_data_pim_03.LoginData.empname)
        search_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_03.LocatorData.search)))
        search_tab.click()
        check = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_pim_03.LocatorData.checkbox)))
        check.click()
        delete_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_pim_03.LocatorData.delete)))
        delete_tab.click()
        delete_prompt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_pim_03.LocatorData.delete_button)))
        delete_prompt.click()


