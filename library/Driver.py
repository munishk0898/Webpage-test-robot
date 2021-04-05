from selenium import webdriver

driver = None


def Initialize():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    load_url = driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    return load_url


def CloseDriver():
    global driver
    driver.quit()
