from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string

def register():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    time.sleep(3)

    # Assert title
    try:
        assert "Automation Exercise" in driver.title
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")

    # Click on SignUp and Login
    signup_login = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    signup_login.click()

    # Fill Name
    name = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    name.send_keys("Salman Khan")

    time.sleep(2)

    # Generate random email
    rand_mail = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    full_mail = f"{rand_mail}@mailinator.com"
    print(f"Generated email: {full_mail}")

    # Fill Email
    email_input = driver.find_element(By.XPATH, "(//input[@data-qa='signup-email'])[1]")
    email_input.send_keys(full_mail)

    time.sleep(2)

    # Click Signup Button
    signup_button = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")
    signup_button.click()
    time.sleep(2)

    # Fill in the signup form
    sex_title = driver.find_element(By.ID, "id_gender1")
    sex_title.click()

    password = driver.find_element(By.ID, "password")
    password.send_keys("Test@1234")

    # Date of Birth
    day = Select(driver.find_element(By.ID, "days"))
    day.select_by_value("10")

    month = Select(driver.find_element(By.ID, "months"))
    month.select_by_value("10")

    year = Select(driver.find_element(By.ID, "years"))
    year.select_by_value("1999")

    time.sleep(5)
    driver.quit()

register()
