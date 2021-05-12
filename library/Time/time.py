"""
This script has methods to navigate
the elements and get the dropdown elements if any under
the same elements in time section
"""
import logging
from selenium.webdriver.common.by import By
from library import page
import library.driver as D

TIME = (By.ID, 'menu_time_viewTimeModule')
TIME_LIST = (By.XPATH, '//*[@id="menu_admin_ProjectInfo"]/parent::li/parent::ul/li')
TIME_SHEETS = (By.XPATH, '//*[@id="menu_time_Timesheets"]')
TIME_SHEETS_LIST = (By.XPATH, '//*[@id="menu_time_viewMyTimesheet"]'
                              '/parent::li/parent::ul/li')
ATTENDANCE = (By.CSS_SELECTOR, '#menu_attendance_Attendance')
ATTENDANCE_LIST = (By.XPATH, '//*[@id="menu_attendance_viewMyAttendanceRecord"]'
                             '/parent::li/parent::ul/li')
REPORTS = (By.ID, 'menu_time_Reports')
REPORTS_LIST = (By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[4]/ul/li[3]/ul/li')
PROJECT_INFO = (By.XPATH, '//*[@id="menu_admin_ProjectInfo"]')
PROJECT_INFO_LIST = (By.XPATH, '//*[@id="menu_admin_viewCustomers"]'
                               '/parent::li/parent::ul/li')


def get_time_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(TIME):
        elements = D.driver.find_elements(*TIME_LIST)
        return page.get_list_text(elements)
    else:
        logging.error('Empty list found in time dropdown')
        return []


def navigate_to_time_sheet():
    """
    This method is used to help to navigate apply button
    :return: True|False
    """
    if page.click_element(TIME):
        if page.click_element(TIME_SHEETS):
            return True
        else:
            logging.error('TIME_SHEETS web element not found')
            return False
    else:
        logging.error('TIME web element not found')
        return False


def navigate_to_attendance():
    """
    This method is used to help to navigate apply button
    :return: True|False
    """
    if page.click_element(TIME):
        if page.click_element(ATTENDANCE):
            return True
        else:
            logging.error('ATTENDANCE web element not found')
            return False
    else:
        logging.error('TIME web element not found')
        return False


def navigate_to_report():
    """
    This method is used to help to navigate apply button
    :return: True|False
    """
    if page.click_element(TIME):
        if page.click_element(REPORTS):
            return True
        else:
            logging.error('REPORTS web element not found')
            return False
    else:
        logging.error('TIME web element not found')
        return False


def navigate_to_project_info():
    """
    This method is used to help to navigate apply button
    :return: True|False
    """
    if page.click_element(TIME):
        if page.click_element(PROJECT_INFO):
            return True
        else:
            logging.error('PROJECT_INFO web element not found')
            return False
    else:
        logging.error('TIME web element not found')
        return False


def get_time_sheet_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(TIME):
        if page.click_element(TIME_SHEETS):
            elements = D.driver.find_elements(*TIME_SHEETS_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in time sheet dropdown')
            return []
    else:
        logging.error('TIME web element not found')
        return False


def get_attendance_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(TIME):
        if page.click_element(TIME_SHEETS):
            elements = D.driver.find_elements(*ATTENDANCE_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in attendance dropdown')
            return []
    else:
        logging.error('TIME web element not found')
        return False


def get_reports_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(TIME):
        if page.click_element(TIME_SHEETS):
            elements = D.driver.find_elements(*REPORTS_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in report dropdown')
            return []
    else:
        logging.error('TIME web element not found')
        return False


def get_project_info_dropdown():
    """
    This method gives the list of elements under the entitlement button
    :return:
    """
    if page.click_element(TIME):
        if page.click_element(TIME_SHEETS):
            elements = D.driver.find_elements(*PROJECT_INFO)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in PROJECT_INFO dropdown')
            return []
    else:
        logging.error('TIME web element not found')
        return False
