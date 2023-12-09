from selenium.webdriver import Chrome
import pytest


@pytest.fixture
def setup():
    driver = Chrome()
    driver.get("http://localhost:8080/login.do")
    driver.maximize_window()
    yield driver
    driver.close()
