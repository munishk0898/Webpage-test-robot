from data import Webpage_elements as data
import pytest
import library.Driver as D
from library import Login
from library.PIM import pim


def setup():
    D.Initialize()


def test_pim_configuration_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_configuration()


def test_pim_configuration_dropdown():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.get_configuration_dropdown() == data.PIM_CONFIGURATION_DROPDOWN


def test_pim_employee_list_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_employee_list()


def test_pim_add_employee_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_add_employee()


def test_pim_report_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert pim.navigate_to_report()


def teardown():
    D.CloseDriver()
