from Generic.Read_Excel import *

loc = read_locator("LoginPage")
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def username(self, data):
        #self.driver.find_element("name", "username").send_keys(data)
        self.driver.find_element(*loc["username"]).send_keys(data)
    def password(self, data):
        #self.driver.find_element("name", "pwd").send_keys(data)
        self.driver.find_element(*loc["password"]).send_keys(data)
    def login_btn(self):
        #self.driver.find_element("xpath", "//div[.='Login ']").click()
        self.driver.find_element(*loc["login_btn"]).click()