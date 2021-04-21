import time
import logging
from selenium.webdriver.common.by import By
import library.Driver as D
from library import page

USER_MANAGEMENT = (By.ID, "menu_admin_UserManagement")
USERS = (By.ID, 'menu_admin_viewSystemUsers')
USER_NAME = (By.ID, 'searchSystemUser_userName')
USER_ROLE = (By.ID, 'searchSystemUser_userType')
USER_MANAGEMENT_LIST = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[1]/ul/li')
EMPLOYEE_NAME = (By.NAME, 'searchSystemUser[employeeName][empName]')
STATUS = (By.XPATH, '//*[@id="searchSystemUser_status"]')
SEARCH = (By.ID, 'searchBtn')
RESET = (By.NAME, '_reset')
ADD = (By.ID, 'btnAdd')
DELETE = (By.ID, 'btnDelete')
ALERT = (By.CLASS_NAME, 'message warning')


def search_user(user_details):
    D.driver.find_element(*USER_NAME).send_keys(user_details[0])
    page.click_element(USER_ROLE)
    page.select_by_text(USER_ROLE, user_details[1])
    D.driver.find_element(*EMPLOYEE_NAME).send_keys(user_details[2])
    page.select_by_text(STATUS, user_details[3])
    if page.get_text(SEARCH):
        return page.get_text(SEARCH)
    else:
        return ""
