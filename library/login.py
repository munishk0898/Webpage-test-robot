"""
This script has the methods like login and driver related functions
"""
import time
import logging
from selenium.webdriver.common.by import By
import library.driver as D

USERNAME_INPUT = (By.NAME, 'txtUsername')
PASSWORD_INPUT = (By.NAME, 'txtPassword')
FORGOT_PASSWORD = (By.ID, 'forgotPasswordLink')
LOGIN_BUTTON = (By.NAME, 'Submit')
ERROR_MESSAGE = (By.ID, 'spanMessage')


def is_url_reachable():
    """

    :return: driver title
    """
    D.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    if D.driver.title:
        logging.info("The Url is reachable")
        return D.driver.title
    else:
        logging.error("The URL is not reachable")


def web_login(user):
    """

    :param user:
    :return: None
    """
    username = user[0]
    password = user[1]
    D.driver.find_element(*USERNAME_INPUT).send_keys(username)
    D.driver.find_element(*PASSWORD_INPUT).send_keys(password)
    D.driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(5)


def expect_wrong_login_message():
    """

    :return:
    """
    message = D.driver.find_element(*ERROR_MESSAGE)
    if message:
        logging.info("Expected Error message: %s", message.text)
        return message.text
    else:
        logging.error("Expected error Message not found")
        raise Exception("Error Message not found")


def get_current_url():
    """
    This method gives the current url of the webpage
    :return: current_url of the webpage
    """
    return D.driver.current_url


def current_driver_title():
    """
    This method helps to get the driver title
    :return: current page title
    """
    return D.driver.title
