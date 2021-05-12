import logging
from library import login
from data import Webpage_elements as data
import pytest
import library.driver as D


def setup():
    """
    Setup function to initialize the driver instance
    :return:
    """
    D.initialize()


def test_is_url_reachable():
    """
    This test function validates the url is reachable or not
    :return:
    """
    assert login.is_url_reachable()


def test_login():
    """
    This test function ensure the login is working for the correct user name nad password
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE


def test_login_with_wrong_user_name():
    """
    Test function assures the login ids rejected for wrong creds
    :return:
    """
    login.web_login(data.WRONG_USER_1)
    assert login.expect_wrong_login_message() == data.LOGIN_MESSAGE_WRONG_CREDS
    assert login.get_current_url() != data.DASHBOARD_URL


def test_login_with_wrong_password():
    """
    Test function assures the login ids rejected for wrong creds
    :return:
    """
    login.web_login(data.WRONG_USER_2)
    assert login.expect_wrong_login_message() == data.LOGIN_MESSAGE_WRONG_CREDS
    assert login.get_current_url() != data.DASHBOARD_URL


def test_login_with_empty_inputs():
    """
    Test function assures the login ids rejected for empty creds
    :return:
    """
    login.web_login(data.EMPTY_USER)
    assert login.expect_wrong_login_message() == data.LOGIN_MESSAGE_EMPTY_INPUT
    assert login.get_current_url() != data.DASHBOARD_URL


def teardown():
    """
    Teardown method which close the driver instance
    :return:
    """
    D.closedriver()
