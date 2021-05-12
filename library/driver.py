"""
This script has the driver related methods like
initialize and close the driver instance
"""
from selenium import webdriver
driver = None


def initialize():
    """
    This method intialize the driver instance for the web driver
    :return: url get object
    """
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    load_url = driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    return load_url


def closedriver():
    """
    This method helps to close the drive rinstance
    :return: None
    """
    global driver
    driver.quit()
