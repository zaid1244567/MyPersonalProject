from Generic.Verify_Title import *
from POM.LoginPage import *
from POM.HomePage import *

def test_Testcase1(setup):
    driver = setup
    verify_title(driver, "actiTIME - Login")
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_btn()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h = HomePage(driver)
    h.logout()
    verify_title(driver, "actiTIME - Login")




