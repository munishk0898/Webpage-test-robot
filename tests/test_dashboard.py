from data import Webpage_elements as data
import pytest
import library.Driver as D
from library import Login
from library.Admin import admin


def setup():
    D.Initialize()


def test_user_navigation():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.navigate_to_users()


def test_user_dropdown():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.get_users_dropdown() == data.USERS_DROPDOWN


def test_job_navigation():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.navigate_to_users()


def test_job_dropdown():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.get_job_dropdown() == data.JOB_DROPDOWN


def test_organization_navigation():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.navigate_to_organization()


def test_organization_dropdown():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    print(admin.get_configuration_dropdown())


def test_qualification_navigation():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.navigate_to_qualifications()


def test_qualification_dropdown():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    print(admin.get_qualifications_dropdown())


def test_configuration_navigation():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.navigate_to_configuration()


def test_configuration_dropdown():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    print(admin.get_configuration_dropdown())


def teardown():
    D.CloseDriver()
