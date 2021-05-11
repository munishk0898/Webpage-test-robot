import logging
from selenium.webdriver.common.by import By
import library.Driver as D
from library import page

PIM = (By.ID, 'menu_pim_viewPimModule')
CONFIGURATION = (By.ID, 'menu_pim_Configuration')
EMPLOYEE_LIST = (By.XPATH, '//*[@id="menu_pim_viewEmployeeList"]')
ADD_EMPLOYEE = (By.ID, 'menu_pim_addEmployee')
REPORT = (By.CSS_SELECTOR, '#menu_core_viewDefinedPredefinedReports')
CONFIGURATION_LIST = (By.XPATH, '//*[@id="menu_pim_configurePim"]/parent::li/parent::ul/li')


def navigate_to_configuration():
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
    if page.click_element(PIM):
        if page.click_element(REPORT):
            return True
        else:
            logging.error('ADD_EMPLOYEE web element not found')
            return False
    else:
        logging.error(' REPORT web element not found')
        return False
