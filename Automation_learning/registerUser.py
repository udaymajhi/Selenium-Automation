from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
time.sleep(3)

#Asserting value
try:
    assert "Automation Exercise" in driver.title
    print("Home page is visible")

except AssertionError:
    print("Home page is not visible")

#Click on SignUp and Login
signUp_login = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']")
signUp_login.click()

#SignUp Verify 'New User Signup!' is visible
name = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
name.send_keys("Uday Majhi")

email = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
email.send_keys("uday@mailinator.com")

signup_button = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']")
signup_button.click()


time.sleep(3)
driver.quit()