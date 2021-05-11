from data import Webpage_elements as data
import pytest
import library.Driver as D
from library import Login
from library.Admin import admin
from library.Admin import users


def setup():
    D.Initialize()


def test_add_user():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()
    assert users.add_user(data.TEST_USER_FOR_ADD)


def test_search_user():
    assert Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()
    assert users.search_user(data.TEST_USER) == data.SUCCESS_MESSAGE


def teardown():
    D.CloseDriver()
