import time
import logging
from selenium.webdriver.common.by import By
import library.Driver as D
from library import page

LEAVE = (By.XPATH, '//*[@id="menu_leave_viewLeaveModule"]')
APPLY_LEAVE = (By.ID, 'menu_leave_applyLeave')
MY_LEAVE = (By.ID, 'menu_leave_viewMyLeaveList')
ENTITLEMENTS = (By.CSS_SELECTOR, '#menu_leave_Entitlements')
REPORTS = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[3]/ul/li[4]')
CONFIGURE = (By.ID, 'menu_leave_Configure')
LEAVE_LIST = (By.XPATH, '//*[@id="menu_leave_viewLeaveList"]')
ASSIGN_LEAVE = (By.CSS_SELECTOR, '#menu_leave_assignLeave')
ENTITLEMENTS_LIST = (By.XPATH, '//*[@id="menu_leave_addLeaveEntitlement"]/parent::li/parent::ul/li')
REPORTS_LIST = (By.XPATH, '//*[@id="menu_leave_viewLeaveBalanceReport"]/parent::li/parent::ul/li')
CONFIGURE_LIST = (By.XPATH, '//*[@id="menu_leave_defineLeavePeriod"]/parent::li/parent::ul/li')


def navigate_to_apply():
    if page.click_element(LEAVE):
        if page.click_element(APPLY_LEAVE):
            return True
        else:
            logging.error('APPLY web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def navigate_to_my_leave():
    if page.click_element(LEAVE):
        if page.click_element(MY_LEAVE):
            return True
        else:
            logging.error('MY_LEAVE web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def navigate_to_entitlements():
    if page.click_element(LEAVE):
        if page.click_element(ENTITLEMENTS):
            return True
        else:
            logging.error('ENTITLEMENTS web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def navigate_to_report():
    if page.click_element(LEAVE):
        if page.click_element(REPORTS):
            return True
        else:
            logging.error('REPORTS web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def navigate_to_configure():
    if page.click_element(LEAVE):
        if page.click_element(CONFIGURE):
            return True
        else:
            logging.error('CONFIGURE web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def navigate_to_leavelist():
    if page.click_element(LEAVE):
        if page.click_element(LEAVE_LIST):
            return True
        else:
            logging.error('LEAVE_LIST web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def navigate_to_assignleave():
    if page.click_element(LEAVE):
        if page.click_element(ASSIGN_LEAVE):
            return True
        else:
            logging.error('ASSIGN_LEAVE web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False
