class LocatorsData:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    User_management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    Job = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
    Organization = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span'
    Qualification = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span'
    Nationalities = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a'
    Corporate_Banking = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]'
    Configuration = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'


class LoginPage:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

# pytest test_code_02.py --html=report.html