"""
This scripts covers the navigation of the modules under the time section in dashboard page.
"""
from data import Webpage_elements as data
import library.driver as D
from library import login
from library.Time import time


def setup():
    """
    Setup function to initialize the driver instance
    :return: None
    """
    D.initialize()


def test_time_dropdown():
    """
    Test function to get the list elements under time
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert time.get_time_dropdown() == data.TIME_LIST


def test_time_sheet_navigation():
    """
    Test function to navigation of time sheet module under time
    :return: None
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert time.navigate_to_time_sheet()


def test_time_sheet_dropdown():
    """
    Test function to get the list elements under time sheet.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    print(time.get_time_sheet_dropdown())


def test_attendance_navigation():
    """
    Test function to navigation of attendance module under time
    :return: None
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert time.navigate_to_attendance()


def test_attendance_dropdown():
    """
    Test function to get the list elements under attendance section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    print(time.get_attendance_dropdown())


def test_report_navigation():
    """
    Test function to navigation of report module under time
    :return: None
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert time.navigate_to_report()


def test_report_dropdown():
    """
    Test function to get the list elements under report section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    print(time.get_reports_dropdown())


def test_project_info_navigation():
    """
    Test function to navigation of project_info module under time
    :return: None
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert time.navigate_to_project_info()


def test_project_info_dropdown():
    """
    Test function to get the list elements under project_info section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    print(time.get_project_info_dropdown())


def teardown():
    """
    Teardown method which close the driver instance
    :return:
    """
    D.closedriver()
