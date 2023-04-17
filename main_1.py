import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initializing the webdriver and wait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

FIRST_NAME = "Rizwana"
LAST_NAME = "Begum"

# Test case ID: TC_Login_01


def test_login_positive():

    # Navigating to the OrangeHRM login page
    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:

        # entering login credentials
        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        username.send_keys("Admin")

        password = wait.until(
            EC.presence_of_element_located((By.NAME, "password")))
        password.send_keys("admin123")

        # pressing login button
        login_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        login_button.click()
        time.sleep(5)
        driver.find_element(
            By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(5)

    except NoSuchElementException:
        print("Error occured while logging into the page")


# Test case ID: TC_Login_02
def test_login_negative():
    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    try:

        # entering invalid login credentials
        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        username.send_keys("Admin")

        password = wait.until(
            EC.presence_of_element_located((By.NAME, "password")))
        password.send_keys("Invalid password")

        # pressing login button
        login_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
        login_button.click()

    finally:
        time.sleep(5)
        driver.quit()


# Test case ID: TC_PIM_01
def test_add_employee_details():

    # calling the login function
    test_login_positive()
    time.sleep(5)

    pim_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')))
    pim_button.click()

    add_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')))
    add_button.click()

    first_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ' #app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(1) > div:nth-child(2) > input')))
    first_name.send_keys(FIRST_NAME)

    time.sleep(5)

    last_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(3) > div:nth-child(2) > input')))
    last_name.send_keys(LAST_NAME)

    time.sleep(5)

    save_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')))
    save_button.click()

    time.sleep(10)

# Test case ID: TC_PIM_02


def test_edit_employee_details():

    # calling the login function
    test_add_employee_details()
    time.sleep(8)

    employee_details_tab = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')))
    employee_details_tab.click()

    time.sleep(5)

    search_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')))
    search_input.send_keys(FIRST_NAME)

    time.sleep(5)

    search_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
    search_button.click()

    time.sleep(5)

    edit_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '// *[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]')))
    edit_button.click()

    time.sleep(8)

# Test case ID: TC_PIM_03


def test_delete_employee_details():
    
    test_add_employee_details()
    time.sleep(8)

    employee_details_tab = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')))
    employee_details_tab.click()

    time.sleep(5)

    search_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')))
    search_input.send_keys(FIRST_NAME)

    time.sleep(5)

    search_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
    search_button.click()

    time.sleep(5)

    delete_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]')))
    delete_button.click()

    time.sleep(5)

    confirm_delete_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')))
    confirm_delete_button.click()
    
