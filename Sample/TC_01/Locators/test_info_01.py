class Data:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"


class LoginPage:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

# pytest test_login_01.py --html=report.html
