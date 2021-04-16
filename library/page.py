import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import library.Driver as D


def click_element(element):
    if element:
        D.driver.find_element(*element).click()
        return True
    else:
        raise Exception("Empty Element")


def get_text(element):
    if element:
        a = D.driver.find_element(*element).text
        print(a)
        print(type(a))
        return a
    else:
        raise Exception("Empty Element")


def select_by_text(drop_down, element):
    select = Select(D.driver.find_element(*drop_down))
    select.select_by_visible_text(element)


def get_list_text(elements):
    list_text_elements = []
    for i in elements:
        list_text_elements.append(i.text)
    return list_text_elements
