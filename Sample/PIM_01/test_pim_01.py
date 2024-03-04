from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from Locators import test_data_pim_1


class CasePim01:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def enable_setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, test_data_pim_1.LoginData.username_input_box).send_keys(
            test_data_pim_1.EmployeeDetails.username)
        self.driver.find_element(By.NAME, test_data_pim_1.LoginData.password_input_box).send_keys(
            test_data_pim_1.EmployeeDetails.password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_1.LoginData.login_xpath)))
        login_button.click()

    def navigate_to_pim(self):
        self.driver.find_element(By.XPATH, test_data_pim_1.AccessEmployee.pim_tab).click()
        self.driver.find_element(By.XPATH, test_data_pim_1.AccessEmployee.add_employee).click()
        self.driver.find_element(By.NAME, test_data_pim_1.AccessEmployee.firstname_input_box).send_keys(
            test_data_pim_1.EmployeeDetails.firstName)
        self.driver.find_element(By.NAME, test_data_pim_1.AccessEmployee.middlename_input_box).send_keys(
            test_data_pim_1.EmployeeDetails.middleName)
        self.driver.find_element(By.NAME, test_data_pim_1.AccessEmployee.lastname_input_box).send_keys(
            test_data_pim_1.EmployeeDetails.lastName)
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, test_data_pim_1.AccessEmployee.save_button)))
        save.click()


CasePim01().enable_setup()
CasePim01().login()
CasePim01().navigate_to_pim()
