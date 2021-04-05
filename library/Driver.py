from selenium import webdriver

driver = None


def Initialize():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    load_url = driver.get("https://www.phptravels.net/admin")
    return load_url


def CloseDriver():
    global driver
    driver.quit()
