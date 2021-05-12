"""
THis test script has functionality test of users related functions.
"""
from data import Webpage_elements as data
import library.driver as D
from library import login
from library.Admin import admin
from library.Admin import users


def setup():
    """
    Setup function to initialize the driver instance
    :return:
    """
    D.initialize()


def test_add_user():
    """
    This test function assures the add user functionality
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()
    assert users.add_user(data.TEST_USER_FOR_ADD)


def test_search_user():
    """
    THis test function validates the search functionality.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert admin.navigate_to_users()
    assert users.search_user(data.TEST_USER) == data.SUCCESS_MESSAGE


def teardown():
    """
    Teardown method which close the driver instance
    :return:
    """
    D.closedriver()
