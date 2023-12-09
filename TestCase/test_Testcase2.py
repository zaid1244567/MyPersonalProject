from Generic.Verify_Title import *
from POM.LoginPage import *
from POM.HomePage import *
from POM.UserPage import *

def test_Testcase2(setup):
    driver = setup
    verify_title(driver, "actiTIME - Login")
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_btn()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h = HomePage(driver)
    h.users_tab()
    verify_title(driver, "actiTIME - User List")
    u = UserPage(driver)
    u.users_btn()
    u.first_name("Selenium")
    u.last_name("Automation")
    u.email("seleniumautomation@gmail.com")
    u.username("seleniumauto")
    u.password("selenium@123")
    u.retype_pwd("selenium@123")
    u.create_user_btn()
    u.username_text()
    h.logout()
    verify_title(driver, "actiTIME - Login")





