from data import Webpage_elements as data
import pytest
import library.driver as D
from library import login
from library.PIM import pim


def setup():
    """
    Setup function to initialize the driver instance
    :return:
    """
    D.initialize()


def test_pim_configuration_navigation():
    """
    Test function to assure navigation of configuration module under pim
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_configuration()


def test_pim_configuration_dropdown():
    """
    Test function to validate the
    drop down elements under pim configuration
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.get_configuration_dropdown() == data.PIM_CONFIGURATION_DROPDOWN


def test_pim_employee_list_navigation():
    """
    Test function to assure navigation of employee_list module under pim
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_employee_list()


def test_pim_add_employee_navigation():
    """
    Test function to assure navigation of add_employee module under pim
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_add_employee()


def test_pim_report_navigation():
    """
    Test function to assure navigation of report module under pim
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_report()


def teardown():
    """
    Teardown method which close the driver instance
    :return:
    """
    D.closedriver()
