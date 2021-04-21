import time
import logging
from selenium.webdriver.common.by import By
import library.Driver as D
from library import page

ADMIN = (By.ID, "menu_admin_viewAdminModule")
USER_MANAGEMENT = (By.ID, "menu_admin_UserManagement")
USER_MANAGEMENT_LIST = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[1]/ul/li')
USERS = (By.ID, 'menu_admin_viewSystemUsers')
JOB = (By.ID, 'menu_admin_Job')
JOB_LIST = (By.XPATH, '//*[@id="menu_admin_viewJobTitleList"]/parent::li/parent::ul/li')
ORGANIZATION = (By.ID, 'menu_admin_Organization')
ORGANIZATION_LIST = (By.XPATH, '//*[@id="menu_admin_viewOrganizationGeneralInformation"]/parent::li/parent::ul/li')
QUALIFICATIONS = (By.ID, 'menu_admin_Qualifications')
QUALIFICATIONS_LIST = (By.XPATH, '//*[@id="menu_admin_viewSkills"]/parent::li/parent::ul/li')
CONFIGURATION = (By.ID, 'menu_admin_Configuration')
CONFIGURATION_LIST = (By.XPATH, '//*[@id="menu_admin_listMailConfiguration"]/parent::li/parent::ul/li')


def navigate_to_users():
    if page.click_element(ADMIN):
        if page.click_element(USER_MANAGEMENT):
            elements = D.driver.find_elements(*USER_MANAGEMENT_LIST)
            if page.click_element(USERS):
                return True
            else:
                logging.error('USERS web element not found')
                return False
        else:
            logging.error(' USER_MANAGEMENT web element not found')
            return False
    else:
        logging.error('Admin web element not found')
        return False


def get_users_dropdown():
    if page.click_element(ADMIN):
        if page.click_element(USER_MANAGEMENT):
            elements = D.driver.find_elements(*USER_MANAGEMENT_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in user dropdown')
            return False
    else:
        logging.error('Admin web element not found')
        return False


def navigate_to_job():
    if page.click_element(ADMIN):
        if page.click_element(JOB):
            return True
        else:
            logging.error('JOB web element not found')
            return False
    else:
        logging.error('Admin web element not found')
        return False


def get_job_dropdown():
    if page.click_element(ADMIN):
        if page.click_element(JOB):
            elements = D.driver.find_elements(*JOB_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in job dropdown')
            return []
    else:
        logging.error('Admin web element not found')
        return False


def navigate_to_organization():
    if page.click_element(ADMIN):
        if page.click_element(ORGANIZATION):
            return True
        else:
            logging.error('ORGANIZATION web element not found')
            return False
    else:
        logging.error('Admin web element not found')
        return False


def get_organization_dropdown():
    if page.click_element(ADMIN):
        if page.click_element(ORGANIZATION):
            elements = D.driver.find_elements(*ORGANIZATION_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in Organization dropdown')
            return []
    else:
        logging.error('Admin web element not found')
        return False


def navigate_to_qualifications():
    if page.click_element(ADMIN):
        if page.click_element(QUALIFICATIONS):
            return True
        else:
            logging.error('QUALIFICATIONS web element not found')
            return False
    else:
        logging.error('Admin web element not found')
        return False


def get_qualifications_dropdown():
    if page.click_element(ADMIN):
        if page.click_element(QUALIFICATIONS):
            elements = D.driver.find_elements(*QUALIFICATIONS_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in qualifications dropdown')
            return []
    else:
        logging.error('Admin web element not found')
        return False


def navigate_to_configuration():
    if page.click_element(ADMIN):
        if page.click_element(CONFIGURATION):
            return True
        else:
            logging.error('CONFIGURATION web element not found')
            return False
    else:
        logging.error('Admin web element not found')
        return False


def get_configuration_dropdown():
    if page.click_element(ADMIN):
        if page.click_element(CONFIGURATION):
            elements = D.driver.find_elements(*CONFIGURATION_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in CONFIGURATION dropdown')
            return []
    else:
        logging.error('Admin web element not found')
        return False
