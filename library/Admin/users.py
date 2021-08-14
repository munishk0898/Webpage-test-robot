"""
This script has the methods to create a user ,search,user and delete the user under admin
"""
import logging
from selenium.webdriver.common.by import By
import library.driver as D
from library import page

USER_MANAGEMENT = (By.ID, "menu_admin_UserManagement")
USERS = (By.ID, 'menu_admin_viewSystemUsers')
USER_NAME = (By.ID, 'searchSystemUser_userName')
# ADD_USER
ADD_USER_ROLE = (By.ID, 'systemUser_userType')
ESS_USER_ROLE = (By.XPATH, '//*[@id="systemUser_userType"]/option[2]')
ADMIN_USER_ROLE = (By.XPATH, '//*[@id="systemUser_userType"]/option[1]')
ADD_EMPLOYEE_NAME = (By.ID, 'systemUser_employeeName_empName')
ADD_USER_NAME = (By.XPATH, '//*[@id="systemUser_userName"]')
STATUS = (By.XPATH, '//*[@id="searchSystemUser_status"]')
ENABLED_USER_STATUS = (By.XPATH, '//*[@id="systemUser_status"]/option[1]')
DISABLED_USER_STATUS = (By.XPATH, '//*[@id="systemUser_status"]/option[2]')
PASSWORD = (By.XPATH, '//input[@id="systemUser_password"]')
CONFIRM_PASSWORD = (By.XPATH, '//input[@id="systemUser_confirmPassword"]')
SAVE = (By.XPATH, '//*[@class="addbutton"]')
USER_MANAGEMENT_LIST = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[1]/ul/li')
# SEARCH_USER
SEARCH_USER_NAME = (By.ID, 'searchSystemUser_userName')
SEARCH_USER_ROLE = (By.ID, 'searchSystemUser_userType')
ALL_USER_ROLE_SEARCH = (By.XPATH, '//*[@id="searchSystemUser_userType"]/option[0]')
ADMIN_USER_ROLE_SEARCH = (By.XPATH, '//*[@id="searchSystemUser_userType"]/option[1]')
ESS_USER_ROLE_SEARCH = (By.XPATH, '//*[@id="searchSystemUser_userType"]/option[2]')
SEARCH_EMPLOYEE_NAME = (By.NAME, 'searchSystemUser[employeeName][empName]')
STATUS_SEARCH = (By.ID, 'searchSystemUser_status')
ALL_STATUS_SEARCH = (By.XPATH, '//*[@id="searchSystemUser_status"]/option[1]')
ENABLED_STATUS_SEARCH = (By.XPATH, '//*[@id="searchSystemUser_status"]/option[2]')
DISABLED_STATUS_SEARCH = (By.XPATH, '//*[@id="searchSystemUser_status"]/option[3]')
SEARCH = (By.ID, 'searchBtn')
RESET = (By.NAME, '_reset')
ADD = (By.ID, 'btnAdd')
DELETE = (By.ID, 'btnDelete')
ALERT = (By.CLASS_NAME, 'message warning')


def select_user_role(user_role):
    """
    This method will select the user role for the specified user
    :param user_role:
    :return:  True | False
    """
    page.click_element(ADD_USER_ROLE)
    if user_role == 'ESS':
        page.click_element(ESS_USER_ROLE)
        return True
    elif user_role == 'Admin':
        page.click_element(ADMIN_USER_ROLE)
        return True
    else:
        logging.error('Invalid user role selected for the user')
        return False


def select_status(user_status):
    """
    This method will select the user status for the specified user
    :param user_status:
    :return: True | False
    """
    if user_status == "Enabled":
        page.click_element(ENABLED_USER_STATUS)
        return True
    elif user_status == "Disabled":
        page.click_element(DISABLED_USER_STATUS)
        return True
    else:
        logging.info('Invalid user status has been selected for the user')
        return False


def add_user(user_info):
    """
    This method helps to add the new user
    :param user_info:
    :return: True | False
    """
    if len(user_info) == 6:
        print(user_info)
        user_role, employee_name, user_name, status, password, confirm_password = user_info
        page.click_element(ADD)
        if select_user_role(user_role):
            page.click_element(ADD_EMPLOYEE_NAME)
            D.driver.find_element(*ADD_EMPLOYEE_NAME).send_keys(employee_name)
            page.click_element(ADD_USER_NAME)
            D.driver.find_element(*ADD_USER_NAME).send_keys(user_name)
        if select_status(status):
            if password == confirm_password:
                D.driver.find_element(*PASSWORD).send_keys(password)
                D.driver.find_element(*CONFIRM_PASSWORD).send_keys(confirm_password)
                page.click_element(SAVE)
                return True
            else:
                logging.info("Password and confirm password fields has"
                             " different elements for %s",user_info)
                return False
    else:
        logging.error("The input information provided for user "
                      "creation doesn't have enough fields")
        return False


def search_user(user_details):
    """
    this methods helps to search the user in the employee list
    :param user_details:
    :return: text or empty string
    """
    D.driver.find_element(*SEARCH_USER_NAME).send_keys(user_details[0])
    page.click_element(SEARCH_USER_ROLE)
    page.select_by_text(SEARCH_USER_ROLE, user_details[1])
    D.driver.find_element(*SEARCH_EMPLOYEE_NAME).send_keys(user_details[2])
    page.select_by_text(STATUS_SEARCH, user_details[3])
    D.driver.find_element(*SEARCH).click()
    if page.get_text(SEARCH):
        print(page.get_text(SEARCH))
        return page.get_text(SEARCH)
    else:
        return ""
