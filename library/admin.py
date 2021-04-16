import time
from selenium.webdriver.common.by import By
import library.Driver as D
from library import page

ADMIN = (By.ID, "menu_admin_viewAdminModule")
USER_MANAGEMENT = (By.ID, "menu_admin_UserManagement")
USER_MANAGEMENT_LIST = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[1]/ul/li')
JOB_LIST = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[2]/ul/li')
USERS = (By.ID, 'menu_admin_viewSystemUsers')
USER_NAME = (By.ID, 'searchSystemUser_userName')
USER_ROLE = (By.ID, 'searchSystemUser_userType')
JOB = (By.ID, 'menu_admin_Job')
EMPLOYEE_NAME = (By.NAME, 'searchSystemUser[employeeName][empName]')
STATUS = (By.XPATH, '//*[@id="searchSystemUser_status"]')
SEARCH = (By.ID, 'searchBtn')
RESET = (By.NAME, '_reset')
ADD = (By.ID, 'btnAdd')
DELETE = (By.ID, 'btnDelete')
ALERT = (By.CLASS_NAME, 'message warning')


def navigate_to_users():
    if page.click_element(ADMIN):
        if page.click_element(USER_MANAGEMENT):
            elements = D.driver.find_elements(*USER_MANAGEMENT_LIST)
            if page.click_element(USERS):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_users_dropdown():
    if page.click_element(ADMIN):
        if page.click_element(USER_MANAGEMENT):
            elements = D.driver.find_elements(*USER_MANAGEMENT_LIST)
            return page.get_list_text(elements)
        else:
            return False
    else:
        return False


def navigate_to_job():
    if page.click_element(ADMIN):
        if page.click_element(JOB):
            return True
        else:
            return False
    else:
        return False


def get_job_dropdown():
    if page.click_element(ADMIN):
        elements = D.driver.find_elements(*JOB_LIST)
        print(page.get_list_text(elements))
        return True
    else:
        return False


def search_user(user_details):
    D.driver.find_element(*USER_NAME).send_keys(user_details[0])
    page.click_element(USER_ROLE)
    page.select_by_text(USER_ROLE, user_details[1])
    D.driver.find_element(*EMPLOYEE_NAME).send_keys(user_details[2])
    page.select_by_text(STATUS, user_details[3])
    print(page.get_text(SEARCH))
    # return page.get_text(SEARCH)

