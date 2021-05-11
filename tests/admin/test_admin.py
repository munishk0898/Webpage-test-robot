"""
This scripts covers the navigation of the modules under the admin section in dashboard page.
"""
from data import Webpage_elements as data
import library.Driver as D
from library import Login
from library.Admin import admin


def setup():
    """
    Setup function to initialize the driver instance
    :return:
    """
    D.Initialize()


def test_user_navigation():
    """
    Test function to navigation of user module under admin
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()


def test_user_dropdown():
    """
    Test function to navigation of
    drop down elements under user and verify the required elements
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_users_dropdown() == data.USERS_DROPDOWN


def test_job_navigation():
    """
    Test function to navigation of job module under admin
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()


def test_job_dropdown():
    """
    Test function to navigation of
    drop down elements under user and verify the required elements
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_job_dropdown() == data.JOB_DROPDOWN


def test_organization_navigation():
    """
    Test function to navigation of organization module under admin
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_organization()


def test_organization_dropdown():
    """
    Test function to navigation of
    drop down elements under organization and verify the required elements
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_configuration_dropdown() == data.ORGANIZATION_DROPDOWN


def test_qualification_navigation():
    """
    Test function to navigation of qualification module under admin
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_qualifications()


def test_qualification_dropdown():
    """
    Test function to navigation of
    drop down elements under qualification and verify the required elements
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_qualifications_dropdown() == data.QUALIFICATION_DROPDOWN


def test_configuration_navigation():
    """
    Test function to navigation of configuration module under admin
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_configuration()


def test_configuration_dropdown():
    """
    Test function to navigation of
    drop down elements under configuration and verify the required elements
    :return: None
    """
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_configuration_dropdown() == data.CONFIGURATION_DROPDOWN


def teardown():
    """
    Teardoen method which close the driver instance
    :return:
    """
    D.CloseDriver()
