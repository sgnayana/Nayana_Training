from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker


@given(u'User navigate to the OrangeHRM Login page URL')
def navigate_to_url(context):
    context.url = "https://opensource-demo.orangehrmlive.com/"
    context.driver.get(context.url)
    context.current_url = context.driver.current_url
    context.driver.maximize_window()

@when(u'User enters the valide username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    time.sleep(10)
    context.driver.find_element(By.NAME,"username").send_keys(username)
    context.driver.find_element(By.NAME,"password").send_keys(password)
    
  
@when(u'User clicks on the login button')
def click_login_btn(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(10)
    

@then(u'verify the user logged in successfully')
def verify_user(context):
    status = context.driver.find_element(By.XPATH,"//h6[text()='Dashboard']").is_displayed()
    assert status,  "User Has been logged in Successfully"
    time.sleep(10)
@when(u'User navigates to the PIM module')
def pim_module(context):
    context.driver.find_element(By.XPATH,"//span[text()='PIM']").click()
    time.sleep(5)


@when(u'User clicks on the Add Employee button')
def add_employee(context):
    context.driver.find_element(By.XPATH,"//button[text()=' Add ']").click()
    time.sleep(5)

@when(u'User enters the First Name and Last Name of the employee')
def add_employee_details(context):
    random_data = Faker()
    first_name = random_data.first_name()
    last_name = random_data.last_name()
    context.driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys(first_name)
    context.driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys(last_name)
    context.driver.find_element(By.XPATH,"//input[@name='lastName']").click()
    context.driver.find_element(By.XPATH,"//button[text()=' Save ']").click()


@then(u'verify the employee added successfully')
def employee_verification(context):
    time.sleep(10)
    employee_status = context.driver.find_element(By.XPATH,"//h6[text()='Personal Details']").is_displayed()
    assert employee_status, "Employee has been added successfully"
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
    context.driver.find_element(By.XPATH,"//a[text()='Logout']").click()
    time.sleep(5)
    logut_status = context.driver.find_element(By.XPATH,"//h5[text()='Login']").is_displayed()
    assert logut_status, "User has been logged out successfully"