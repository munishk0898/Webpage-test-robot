import logging
from library import Login
from data import Webpage_elements as data
import pytest
import library.Driver as D


def setup():
    D.Initialize()


def test_is_url_reachable():
    assert Login.is_url_reachable()


def test_login():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE


def test_login_with_wrong_user_name():
    Login.web_login(data.WRONG_USER_1)
    assert Login.expect_wrong_login_message() == data.LOGIN_MESSAGE_WRONG_CREDS
    assert Login.get_current_url() != data.DASHBOARD_URL


def test_login_with_wrong_password():
    Login.web_login(data.WRONG_USER_2)
    assert Login.expect_wrong_login_message() == data.LOGIN_MESSAGE_WRONG_CREDS
    assert Login.get_current_url() != data.DASHBOARD_URL


def test_login_with_empty_inputs():
    Login.web_login(data.EMPTY_USER)
    assert Login.expect_wrong_login_message() == data.LOGIN_MESSAGE_EMPTY_INPUT
    assert Login.get_current_url() != data.DASHBOARD_URL


def teardown():
    D.CloseDriver()
