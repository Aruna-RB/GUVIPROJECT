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
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    # pim_tab = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_employee = "//a[contains(text(),'Add Employee')]"
    save_button = "//button[@type='submit']"
    firstname_input_box = "firstName"
    middlename_input_box = "middleName"
    lastname_input_box = "lastName"

# pytest test_pim_01.py --html=report.html
