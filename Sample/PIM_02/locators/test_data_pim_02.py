class LoginPage:
    username = "Admin"
    password = "admin123"


class ModifyDetails:
    employeeName = "Aruna"
    middleName = "RB"


class Locators:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"


class AccessPim:
    pim_tab = "//a[@href='/web/index.php/pim/viewPimModule']"
    input_box_employeeName = "//input[@placeholder='Type for hints...']"
    search = "//button[@type='submit']"


class UpdateInfo:
    edit = "//i[@class='oxd-icon bi-pencil-fill']"
    middlename_input_box = "middleName"
    save_button = "//button[@type='submit']"
