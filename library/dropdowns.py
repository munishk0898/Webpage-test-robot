import time
from selenium.webdriver.common.by import By
import library.Driver as D




def get_text_list(elements):
    list_text_elements = []
    for i in elements:
        list_text_elements.append(i.text)
    return list_text_elements


def click_dropdown_get_list_elements(label):
    if label == "GENERAL":
        D.driver.find_element(*GENERAL[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*GENERAL[1])
    elif label == 'ACCOUNTS':
        D.driver.find_element(*ACCOUNTS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*ACCOUNTS[1])
    elif label == "CMS":
        D.driver.find_element(*CMS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*CMS[1])
    elif label == "HOTELS":
        D.driver.find_element(*HOTELS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*HOTELS[1])
    elif label == "FLIGHTS":
        D.driver.find_element(*FLIGHTS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*FLIGHTS[1])
    elif label == "BOATS":
        D.driver.find_element(*BOATS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*BOATS[1])
    elif label == "RENTALS":
        D.driver.find_element(*RENTALS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*RENTALS[1])
    elif label == "TOURS":
        D.driver.find_element(*TOURS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*TOURS[1])
    elif label == "CARTRAWLER":
        D.driver.find_element(*CARTRAWLER[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*CARTRAWLER[1])
    elif label == "VISA":
        D.driver.find_element(*VISA[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*VISA[1])
    elif label == "BLOG":
        D.driver.find_element(*BLOG[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*BLOG[1])
    elif label == "LOCATIONS":
        D.driver.find_element(*LOCATIONS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*LOCATIONS[1])
    elif label == "OFFERS":
        D.driver.find_element(*OFFERS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*OFFERS[1])
    elif label == "PAYOUTS":
        D.driver.find_element(*PAYOUTS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*PAYOUTS[1])
    else:
        raise Exception("Expected", label, " dropdown not Found")
    return get_text_list(elements)


def get_text(element):
    label_element = D.driver.find_element(*element)
    return label_element.text


def click_element(element):
    update_str = D.driver.find_element(*element)
    update_str.click()
    return True
