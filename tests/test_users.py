from data import Webpage_elements as data
import pytest
import library.Driver as D
from library import Login
from library import admin


def setup():
    D.Initialize()


def test_search_add():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title
    assert admin.navigate_to_users()
    assert admin.search_user(data.TEST_USER) == data.SUCCESS_MESSAGE


def teardown():
    D.CloseDriver()
