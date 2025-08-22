# register.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random_mail import email_here

def register():
    # Launch browser
    driver = webdriver.Chrome()
    # Navigate to url 'http://automationexercise.com'
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    time.sleep(3)

    # Verify that home page is visible successfully
    try:
        assert "Automation Exercise" in driver.title
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")

    # Click on SignUp and Login
    signup_login = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    signup_login.click()
    time.sleep(2)

    # Verify that home page is visible successfully
    try:
        assert "Automation Exercise - Signup / Login" in driver.title
        print("Sign Up page Visisble")
    except AssertionError:
        print("Sign Up page is not visible")

    # Fill Name
    name = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    name.send_keys("Salman Khan")
    time.sleep(2)

    # Use random email from separate file
    full_mail = email_here()

    # Fill Email
    email_input = driver.find_element(By.XPATH, "(//input[@data-qa='signup-email'])[1]")
    email_input.send_keys(full_mail)
    time.sleep(2)

    # Click Signup button
    signup_button = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")
    signup_button.click()
    time.sleep(2)

    # Fill the signup form
    sex_title = driver.find_element(By.ID, "id_gender1")
    sex_title.click()

    password = driver.find_element(By.ID, "password")
    password.send_keys("Test@1234")

    # Date of birth selects
    day = Select(driver.find_element(By.ID, "days"))
    day.select_by_value("10")

    month = Select(driver.find_element(By.ID, "months"))
    month.select_by_value("10")

    year = Select(driver.find_element(By.ID, "years"))
    year.select_by_value("1999")

    newsletter = driver.find_element(By.ID,"newsletter")
    newsletter.click()

    offers = driver.find_element(By.ID, "optin")
    offers.click()

    first_name = driver.find_element(By.ID,"first_name")
    first_name.send_keys("Salman")

    last_name = driver.find_element(By.ID, "last_name")
    last_name.send_keys("Khan")

    company = driver.find_element(By.ID, "company")
    company.send_keys("Sakhu")

    address1 = driver.find_element(By.ID, "address1")
    address1.send_keys("Sakhuware")

    address2 = driver.find_element(By.ID, "address2")
    address2.send_keys("Gadhi")

    country = Select(driver.find_element(By.ID,"country"))
    country.select_by_value("New Zealand")

    state = driver.find_element(By.ID, "state")
    state.send_keys("Province 1")

    city = driver.find_element(By.ID, "city")
    city.send_keys("New Zea")

    zipcode = driver.find_element(By.ID, "zipcode")
    zipcode.send_keys("46000")

    mobile_number = driver.find_element(By.ID, "mobile_number")
    mobile_number.send_keys("Salman Khan")

    create_account = driver.find_element(By.XPATH,"//button[normalize-space()='Create Account']")
    create_account.click()

    print("Account created successfully")
    time.sleep(8)

    continues = driver.find_element(By.XPATH, "//a[normalize-space()='Continue']")
    continues.click()

    driver.quit()

register()
