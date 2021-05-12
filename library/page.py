"""
This script has the basic function to perform the action in webpage
"""
import logging
from selenium.webdriver.support.select import Select
import library.driver as D


def click_element(element):
    """

    :param element:
    :return: True | exception
    """
    if element:
        D.driver.find_element(*element).click()
        return True
    else:
        logging.error("Empty Element! Not clickable!!!")
        raise Exception("Empty Element! Not clickable!!!")


def get_text(element):
    """
    This method helps to get the text of the web element
    :param element:
    :return: text or empty string
    """
    if element:
        text = D.driver.find_element(*element).text
        return text
    else:
        logging.error('Cannot get text for Empty element')
        return ""


def select_by_text(drop_down, element):
    """
    THis method select the web element with respect text
    :param drop_down:
    :param element:
    :return: None
    """
    select = Select(D.driver.find_element(*drop_down))
    select.select_by_visible_text(element)


def get_list_text(elements):
    """
    THis method helps to get the list of elements under the web element
    :param elements:
    :return: list of elements or empty list
    """
    if elements:
        list_text_elements = []
        for i in elements:
            list_text_elements.append(i.text)
        return list_text_elements
    else:
        logging.info("No list elements found")
        return []
