from Generic.Read_Excel import *

loc = read_locator("HomePage")
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def users_tab(self):
        #self.driver.find_element("xpath", "//div[.='Users']").click()
        self.driver.find_element(*loc["users_tab"]).click()
    def logout(self):
        #self.driver.find_element("xpath", "//a[.='Logout']").click()
        self.driver.find_element(*loc["logout"]).click()