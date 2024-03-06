from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Locators import test_data_03


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

    def test_validate_menu(self, enable_setup):
        self.driver.find_element(By.NAME, test_data_03.LocatorsData.input_box_username).send_keys(
            test_data_03.LoginPage.username)
        self.driver.find_element(By.NAME, test_data_03.LocatorsData.input_box_password).send_keys(
            test_data_03.LoginPage.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_03.LocatorsData.login_xpath)))
        login_button.click()

        admin_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.admin)))
        print(admin_tab.is_displayed())
        pim_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.pim)))
        print(pim_tab.is_displayed())
        leave_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.leave)))
        print(leave_tab.is_displayed())
        time_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.Time)))
        print(time_tab.is_displayed())
        recruitment_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.recruitment)))
        print(recruitment_tab.is_displayed())
        info_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.my_info)))
        print(info_tab.is_displayed())
        performance_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.performance)))
        print(performance_tab.is_displayed())
        dashboard_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.dashboard)))
        print(dashboard_tab.is_displayed())
        directory_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.directory)))
        print(directory_tab.is_displayed())
        maintenance_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.maintenance)))
        print(maintenance_tab.is_displayed())
        buzz_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, test_data_03.LocatorsData.buzz)))
        print(buzz_tab.is_displayed())
