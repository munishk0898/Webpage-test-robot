import time
from selenium.webdriver.common.by import By
import library.Driver as D

USERNAME_INPUT = (By.NAME, 'txtUsername')
PASSWORD_INPUT = (By.NAME, 'txtPassword')
FORGOT_PASSWORD = (By.ID, 'forgotPasswordLink')
LOGIN_BUTTON = (By.NAME, 'Submit')
ERROR_MESSAGE = (By.ID, 'spanMessage')


def is_url_reachable():
    D.driver.get("https://www.phptravels.net/admin")
    return D.driver.title


def web_login(user):
    username = user[0]
    password = user[1]
    D.driver.find_element(*USERNAME_INPUT).send_keys(username)
    D.driver.find_element(*PASSWORD_INPUT).send_keys(password)
    D.driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(5)
    return True


def expect_wrong_login_message():
    message = D.driver.find_element(*ERROR_MESSAGE)
    if message:
        print("Expected Error message: ", message.text)
        return message.text
    else:
        raise Exception("Error Message not found")


def get_current_url():
    return D.driver.current_url


def current_driver_title():
    return D.driver.title
