import time
from selenium.webdriver.common.by import By
import library.Driver as D

USERNAME_INPUT = (By.NAME, 'txtUsername')
PASSWORD_INPUT = (By.NAME, 'txtPassword')
FORGOT_PASSWORD = (By.ID, 'forgotPasswordLink')
LOGIN_BUTTON = (By.NAME, 'Submit')

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


def current_driver_title():
    return D.driver.title
