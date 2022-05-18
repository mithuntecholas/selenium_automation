import time

from selenium import  webdriver
from behave import *
from selenium.webdriver.common.by import By
@given(u'Launch the browser')
def launch_browser(context):
    context.driver=webdriver.Chrome()

@when(u'open the orange hrm website')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@when(u'enter username "{username}"  and password "{password}"')
def step_impl(context,username,password):
    user_text = context.driver.find_element(By.XPATH, "//input[@id='txtUsername']")
    pass_text = context.driver.find_element(By.XPATH, "//input[@id='txtPassword']")
    login_button = context.driver.find_element(By.XPATH, "//input[@id='btnLogin']")
    time.sleep(2)
    user_text.send_keys(username)
    pass_text.send_keys(password)
    login_button.click()


@when(u'click the login button')
def step_impl(context):
    dashboard = context.driver.find_element(By.XPATH, "//b[normalize-space()='Dashboard']")
    assert dashboard.is_displayed() is True



@then(u'User must login to the dashboard page')
def step_impl(context):
    context.driver.quit()

