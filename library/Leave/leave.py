"""
This script has methods to navigate
the elements and get the dropdown elements if any under
the same elements in leave section
"""
import logging
from selenium.webdriver.common.by import By
from library import page
import library.driver as D

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
    """
    This method is used to help to navigate apply button
    :return: True|False
    """
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
    """
    This method is used to help to navigate my_leave button
    :return: True|False
    """
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
    """
    This method is used to help to navigate entitlements button
    :return: True|False
    """
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
    """
    This method is used to help to navigate report button
    :return: True|False
    """
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
    """
    This method is used to help to navigate configure button
    :return: True|False
    """
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
    """
    This method is used to help to navigate leave_list button
    :return: True|False
    """
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
    """
    This method is used to help to navigate assign_leave button
    :return: True|False
    """
    if page.click_element(LEAVE):
        if page.click_element(ASSIGN_LEAVE):
            return True
        else:
            logging.error('ASSIGN_LEAVE web element not found')
            return False
    else:
        logging.error('LEAVE web element not found')
        return False


def get_entitlement_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(LEAVE):
        if page.click_element(ENTITLEMENTS):
            elements = D.driver.find_elements(*ENTITLEMENTS_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in entitlement dropdown')
            return []
    else:
        logging.error('LEAVE web element not found')
        return False


def get_report_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(LEAVE):
        if page.click_element(REPORTS):
            elements = D.driver.find_elements(*REPORTS_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in REPORTS dropdown')
            return []
    else:
        logging.error('LEAVE web element not found')
        return False


def get_configure_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(LEAVE):
        if page.click_element(CONFIGURE):
            elements = D.driver.find_elements(*CONFIGURE_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in CONFIGURE dropdown')
            return []
    else:
        logging.error('LEAVE web element not found')
        return False
