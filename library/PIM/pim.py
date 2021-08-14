"""
This cript holds the methods to navigate the pim elements
and get their dropdown elements if any
"""
import logging
from selenium.webdriver.common.by import By
import library.driver as D
from library import page

PIM = (By.ID, 'menu_pim_viewPimModule')
CONFIGURATION = (By.ID, 'menu_pim_Configuration')
EMPLOYEE_LIST = (By.XPATH, '//*[@id="menu_pim_viewEmployeeList"]')
ADD_EMPLOYEE = (By.ID, 'menu_pim_addEmployee')
REPORT = (By.CSS_SELECTOR, '#menu_core_viewDefinedPredefinedReports')
CONFIGURATION_LIST = (By.XPATH, '//*[@id="menu_pim_configurePim"]/parent::li/parent::ul/li')
FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
CHECK_BOX = (By.ID, 'chkLogin')
USER_NAME = (By.XPATH, '//*[@id="user_name"]')
PASSWORD = (By.CSS_SELECTOR, '#user_password')
CONFIRM_PASSWORD = (By.NAME, 're_password')
SAVE = (By.ID, 'btnSave')


def navigate_to_configuration():
    """
    This method helps to navigate the configuration button
    :return: True|False
    """
    if page.click_element(PIM):
        if page.click_element(CONFIGURATION):
            return True
        else:
            logging.error('CONFIGURATION web element not found')
            return False
    else:
        logging.error(' PIM web element not found')
        return False


def get_configuration_dropdown():
    """
    This method helps to get the list elements under configuration button
    :return: True|False
    """
    if page.click_element(PIM):
        if page.click_element(CONFIGURATION):
            elements = D.driver.find_elements(*CONFIGURATION_LIST)
            return page.get_list_text(elements)
        else:
            logging.error('Empty list found in user dropdown')
            return False
    else:
        logging.error('PIM web element not found')
        return False


def navigate_to_employee_list():
    """
    This method helps to navigate the employee_list button
    :return: True|False
    """
    if page.click_element(PIM):
        if page.click_element(EMPLOYEE_LIST):
            return True
        else:
            logging.error('EMPLOYEE_LIST web element not found')
            return False
    else:
        logging.error(' PIM web element not found')
        return False


def navigate_to_add_employee():
    """
    This method helps to navigate the add_employee_button button
    :return: True|False
    """
    if page.click_element(PIM):
        if page.click_element(ADD_EMPLOYEE):
            return True
        else:
            logging.error('ADD_EMPLOYEE web element not found')
            return False
    else:
        logging.error(' PIM web element not found')
        return False


def navigate_to_report():
    """
    This method helps to navigate the report button
    :return: True|False
    """
    if page.click_element(PIM):
        if page.click_element(REPORT):
            return True
        else:
            logging.error('ADD_EMPLOYEE web element not found')
            return False
    else:
        logging.error(' REPORT web element not found')
        return False


def add_employee(USER_DATA):
    if page.click_element(PIM):
        if page.click_element(ADD_EMPLOYEE):
            D.driver.find_element(*FIRST_NAME).send_keys(USER_DATA[0])
            D.driver.find_element(*LAST_NAME).send_keys(USER_DATA[1])
            page.click_element(CHECK_BOX)
            D.driver.find_element(*USER_NAME).send_keys(USER_DATA[2])
            D.driver.find_element(*PASSWORD).send_keys(USER_DATA[3])
            D.driver.find_element(*CONFIRM_PASSWORD).send_keys(USER_DATA[3])
            page.click_element(SAVE)
