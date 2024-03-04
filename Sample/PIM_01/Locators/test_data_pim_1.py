class EmployeeDetails:
    username = "Admin"
    password = "admin123"
    firstName = "Aruna"
    middleName = "Balaji"
    lastName = "Ragothaman"


class LoginData:
    username_input_box = "username"
    password_input_box = "password"
    login_xpath = "//button[@type='submit']"


class AccessEmployee:
    pim_tab = "//a[@href='/web/index.php/pim/viewPimModule']"
    add_employee = "//a[contains(text(),'Add Employee')]"
    save_button = "//button[@type='submit']"
    firstname_input_box = "firstName"
    middlename_input_box = "middleName"
    lastname_input_box = "lastName"
