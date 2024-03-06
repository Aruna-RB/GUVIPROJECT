class LoginData:
    username = "Admin"
    password = "admin123"
    empname = "Aruna"


class LocatorData:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    pim_tab = "//a[@href='/web/index.php/pim/viewPimModule']"
    input_box_employeeName = "//input[@placeholder='Type for hints...']"
    search = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    checkbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i'
    delete = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button'
    delete_button = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'

 # pytest test_pim_03.py --html=report.html