from data import Webpage_elements as data
import library.Driver as D
from library import Login
from library.Leave import leave


def setup():
    D.Initialize()


def test_leave_apply_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_apply()


def test__navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_apply()


def test_my_leave_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_my_leave()


def test_entitlements_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_entitlements()


def test_leave_report_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_report()


def test_leave_configure_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_configure()


def test_leave_list_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_leavelist()


def test_assign_leave_navigation():
    Login.web_login(data.LOGIN_CREDENTIALS)
    assert Login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_assignleave()


def teardown():
    D.CloseDriver()
