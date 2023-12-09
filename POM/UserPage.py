from Generic.Verify_Text import verify_text
from time import sleep
from Generic.Read_Excel import *

loc = read_locator("UserPage")
class UserPage:
    def __init__(self, driver):
        self.driver = driver

    def users_btn(self):
        #self.driver.find_element("xpath", "//span[.='User']").click()
        self.driver.find_element(*loc["users_btn"]).click()

    def first_name(self, data):
        #self.driver.find_element("name", "firstName").send_keys(data)
        self.driver.find_element(*loc["first_name"]).send_keys(data)

    def last_name(self, data):
        #self.driver.find_element("name", "lastName").send_keys(data)
        self.driver.find_element(*loc["last_name"]).send_keys(data)

    def email(self, data):
        #self.driver.find_element("name", "email").send_keys(data)
        self.driver.find_element(*loc["email"]).send_keys(data)

    def username(self, data):
        #self.driver.find_element("name", "username").send_keys(data)
        self.driver.find_element(*loc["username"]).send_keys(data)

    def password(self, data):
        #self.driver.find_element("name", "password").send_keys(data)
        self.driver.find_element(*loc["password"]).send_keys(data)

    def retype_pwd(self, data):
        #self.driver.find_element("name", "passwordCopy").send_keys(data)
        self.driver.find_element(*loc["retype_pwd"]).send_keys(data)

    def create_user_btn(self):
        #self.driver.find_element("id", "userDataLightBox_commitBtn").click()
        self.driver.find_element(*loc["create_user_btn"]).click()

    def username_text(self):
        sleep(5)
        atext = self.driver.find_element("xpath", "(//div[@class='name'])[1]").text
        verify_text(atext, "Automation, Selenium (seleniumauto)",self.driver)


