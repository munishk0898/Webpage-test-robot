from library import Login
from data import Webpage_elements as data
import pytest
import library.Driver as D


def setup():
    D.Initialize()


def test_is_url_reachable():
    assert Login.is_url_reachable()


def test_login():
    assert Login.web_login(data.login_credentials)
    assert Login.current_driver_title() == data.Dashboard_title


def test_login_with_wrong_user_name():
    assert Login.web_login(data.Wrong_user_1)
    assert Login.expect_wrong_login_message() == data.Login_message_wrong_creds
    assert Login.get_current_url() != data.dashboard_url


def test_login_with_wrong_password():
    assert Login.web_login(data.Wrong_user_2)
    assert Login.expect_wrong_login_message() == data.Login_message_wrong_creds
    assert Login.get_current_url() != data.dashboard_url


def test_login_with_empty_inputs():
    assert Login.web_login(data.Empty_user)
    assert Login.expect_wrong_login_message() == data.Login_message_empty_input
    assert Login.get_current_url() != data.dashboard_url


def teardown():
    D.CloseDriver()
