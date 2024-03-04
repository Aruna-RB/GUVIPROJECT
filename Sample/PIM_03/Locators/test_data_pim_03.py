class LoginData:
    username = "Admin"
    password = "admin123"
    employeeName = "Aruna"


class Locators:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    pim_tab = "//a[@href='/web/index.php/pim/viewPimModule']"
    input_box_employeeName = "//input[@placeholder='Type for hints...']"
    search = "//button[@type='submit']"
    delete = "//i[@class='oxd-icon bi-trash']"
    delete_button = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
