from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import test_data_pim_02


class TestPim02:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_modify_details(self, enable_setup):
        self.driver.find_element(By.NAME, test_data_pim_02.Locators.input_box_username).send_keys(
            test_data_pim_02.LoginPage.username)
        self.driver.find_element(By.NAME, test_data_pim_02.Locators.input_box_password).send_keys(
            test_data_pim_02.LoginPage.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_02.Locators.login_xpath)))
        login_button.click()
        self.driver.find_element(By.XPATH, test_data_pim_02.AccessPim.pim_tab).click()
        self.driver.find_element(By.XPATH, test_data_pim_02.AccessPim.input_box_employeeName).send_keys(
            test_data_pim_02.ModifyDetails.employeeName)
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_02.AccessPim.search)))
        search_box.click()
        self.driver.find_element(By.XPATH, test_data_pim_02.UpdateInfo.edit).click()
        self.driver.find_element(By.NAME, test_data_pim_02.UpdateInfo.middlename_input_box).send_keys(
            test_data_pim_02.ModifyDetails.middleName)
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_02.UpdateInfo.save_button)))
        save.click()
