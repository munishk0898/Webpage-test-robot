import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import library.Driver as D


def click_element(element):
    if element:
        D.driver.find_element(*element).click()
        return True
    else:
        logging.error("Empty Element! Not clickable!!!")
        raise Exception("Empty Element! Not clickable!!!")


def get_text(element):
    if element:
        a = D.driver.find_element(*element).text
        return a
    else:
        logging.error('Cannot get text for Empty element')
        return ""


def select_by_text(drop_down, element):
    select = Select(D.driver.find_element(*drop_down))
    select.select_by_visible_text(element)


def get_list_text(elements):
    if elements:
        list_text_elements = []
        for i in elements:
            list_text_elements.append(i.text)
        return list_text_elements
    else:
        logging.info("No list elements found")
        return []
