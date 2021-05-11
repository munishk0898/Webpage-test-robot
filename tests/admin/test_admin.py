from data import Webpage_elements as data
import pytest
import library.Driver as D
from library import Login
from library.Admin import admin


def setup():
    D.Initialize()


def test_user_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()


def test_user_dropdown():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_users_dropdown() == data.USERS_DROPDOWN


def test_job_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()


def test_job_dropdown():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_job_dropdown() == data.JOB_DROPDOWN


def test_organization_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_organization()


def test_organization_dropdown():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_configuration_dropdown() == data.ORGANIZATION_DROPDOWN


def test_qualification_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_qualifications()


def test_qualification_dropdown():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_qualifications_dropdown() == data.QUALIFICATION_DROPDOWN


def test_configuration_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_configuration()


def test_configuration_dropdown():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.get_configuration_dropdown() == data.CONFIGURATION_DROPDOWN


def teardown():
    D.CloseDriver()
