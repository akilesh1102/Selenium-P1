import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


def login():

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

    except NoSuchElementException:
        print("Error occured while logging into the page")


def search_validation():

    login()
    time.sleep(5)
    try:
        search_bar = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')))

        search_lists = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My info',
                        'Performance', 'Dashboard', 'Directory', 'Maintanence', 'Buzz']
        # normal
        for context in search_lists:
            search_bar.send_keys(context)
            time.sleep(5)
            search_bar.send_keys(Keys.CONTROL + "a")
            search_bar.send_keys(Keys.DELETE)
            time.sleep(2)
        # with small
        for context in search_lists:
            search_bar.send_keys(context.lower())
            time.sleep(5)
            search_bar.send_keys(Keys.CONTROL + "a")
            search_bar.send_keys(Keys.DELETE)
            time.sleep(2)

        print("Validation success")

    except NoSuchElementException:
        print("Error while validating")


def test_add_employee_details():

    # calling the login function
    login()
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


def drop_down_validation():

    login()
    time.sleep(2)

    try:
        admin_bar = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')))
        admin_bar.click()
        time.sleep(2)

        dropdown = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'oxd-select-wrapper')]")))
        dropdown.click()
        time.sleep(2)

    except NoSuchElementException:
        print("Error while validating drop down")


def fill_employee_details_validation():
    test_add_employee_details()

    enable_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='oxd-switch-wrapper']//label")))
    enable_button.click()
    time.sleep(5)

    username = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')))
    username.send_keys('rizwana_begum_2001')
    time.sleep(2)

    status_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//label[normalize-space()='Enabled']")))
    status_button.click()
    time.sleep(2)

    password = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")))
    password.send_keys('Etvoil@007')
    time.sleep(2)

    confirm_password = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")))
    confirm_password.send_keys('Etvoil@007')
    time.sleep(2)

    save_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Save']")))
    save_button.click()
    time.sleep(7)


def employee_personal_details_validation():

    fill_employee_details_validation()
    time.sleep(4)
    # tabs_lists = ['Personal Details','Contact Details','Emergency Contacts','Dependents','Immigration','Job','Salary','Tax Exemptions','Report-to','Qualifications','Memberships']
    for i in range(1, 12):
        tab_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"(//div[@role='tab'])[{i}]")))
        tab_button.click()
        time.sleep(2)


def personal_details_page():

    fill_employee_details_validation()
    time.sleep(8)

    for i in [5, 6, 7, 8, 9, 10, 11, 'nationality', 'marital_status', 12, 'gender', 15, 'save']:
        if type(i) == int:
            btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"(//input)[{i}]")))
        match i:
            case 5:
                btn.send_keys("Rizu")
                time.sleep(5)
            case 6:
                btn.send_keys("8080")
                time.sleep(5)
            case 7:
                btn.send_keys('7575')
                time.sleep(5)
            case 8:
                btn.send_keys('20200000008080')
                time.sleep(5)
            case 9:
                btn.send_keys('2040-01-01')
                time.sleep(5)
            case 10:
                btn.send_keys('470110285')
                time.sleep(5)
            case 11:
                btn.send_keys('20011002')
                time.sleep(5)
            case 'nationality':
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "(//div)[96]"))).send_keys('iii')
                time.sleep(5)
            case 'marital_status':
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "(//div)[104]"))).send_keys('m')
                time.sleep(5)
            case 12:
                btn.send_keys('2001-01-10')
                time.sleep(5)
            case 'gender':
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, ""))).click()
                time.sleep(5)
            case 15:
                btn.send_keys('No')
                time.sleep(5)
            case 'save':
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]"))).click()
                time.sleep(5)


def dependency_details():

    fill_employee_details_validation()
    time.sleep(8)

    dependents_tab = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//a[normalize-space()='Dependents']")))
    dependents_tab.click()
    time.sleep(7)

    add_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='orangehrm-attachment']//button[@type='button'][normalize-space()='Add']")))
    add_button.click()
    time.sleep(5)

    comment_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//textarea[@placeholder='Type comment here'])[1]")))
    comment_box.send_keys("This is a comment")
    time.sleep(5)

    save_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Save']")))
    save_button.click()
    time.sleep(5)


def job_details():
    fill_employee_details_validation()
    time.sleep(8)

    job_tab = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//a[normalize-space()='Job']")))
    job_tab.click()
    time.sleep(7)

    joined_date = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@placeholder='yyyy-mm-dd']")))
    joined_date.send_keys('2001-08-13')
    time.sleep(5)

    job_title = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]")))
    job_title.send_keys('ceo')
    time.sleep(5)

    job_description = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]")))
    job_description('Job description')
    time.sleep(5)

    save_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Save']")))
    save_button.click()
    time.sleep(5)


def tax_exemptions():
    fill_employee_details_validation()
    time.sleep(8)

    tax_tab = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//a[normalize-space() = 'Tax Exemptions']")))
    tax_tab.click()
    time.sleep(7)

    status = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]")))
    status.send_keys('m')
    time.sleep(5)

    exemption = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")))
    exemption.send_keys("contents..")
    time.sleep(5)

    save_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Save']")))
    save_button.click()
    time.sleep(5)
# ------------------------------------------------------------------------------------------------------------------------------------
