from data import Webpage_elements as data
import library.driver as D
from library import login
from library.Leave import leave


def setup():
    """
    Setup function to initialize the driver instance
    :return: None
    """
    D.initialize()


def test_leave_apply_navigation():
    """
    Test function to navigation of leave_apply under leave section.
    :return: None
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_apply()


def test_my_leave_navigation():
    """
    Test function to navigation of my_leave under leave section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_my_leave()


def test_entitlements_navigation():
    """
    Test function to navigation of entitlements under leave section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_entitlements()


def test_entitlements_dropdown():
    """
    Test function to get the list elements under entitlements section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.get_entitlement_dropdown() == data.LEAVE_ENTITLEMENTS_LIST


def test_leave_report_navigation():
    """
    Test function to navigation of report under leave section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_report()


def test_leave_report_dropdown():
    """
    Test function to get the list elements under report section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.get_report_dropdown() == data.LEAVE_REPORT_LIST


def test_leave_configure_navigation():
    """
    Test function to navigation of configure under leave section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_configure()


def test_leave_configure_dropdown():
    """
    Test function to get the list elements under configure section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.get_configure_dropdown() == data.LEAVE_CONFIGURE_LIST


def test_leave_list_navigation():
    """
    Test function to navigation of leave_list under leave section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_leavelist()


def test_assign_leave_navigation():
    """
    Test function to navigation of assign leave under leave section.
    :return:
    """
    login.web_login(data.LOGIN_CREDENTIALS)
    assert login.current_driver_title() == data.DASHBOARD_TITLE
    assert leave.navigate_to_assignleave()


def teardown():
    """
    Teardown method which close the driver instance
    :return:
    """
    D.closedriver()
