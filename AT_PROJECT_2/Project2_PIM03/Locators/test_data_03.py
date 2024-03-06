class LocatorsData:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    pim = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    leave = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span'
    Time = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span'
    recruitment = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'
    my_info = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span'
    performance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span'
    dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span'
    directory = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span'
    maintenance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span'
    buzz = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span'


class LoginPage:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"


# pytest test_code_03.py --html=report.html
