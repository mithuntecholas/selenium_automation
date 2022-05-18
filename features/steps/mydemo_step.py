from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import  By

@given(u'Launch chrome browser')
def launch_browser(context):
    context.driver=webdriver.Chrome()

@when(u'open Orange hrm home page')
def open_site(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@then(u'verify logo present on home page')
def step_impl(context):
    logo = context.driver.find_element(By.XPATH, "//div[@id='divLogo']//img")
    assert logo.is_displayed() is True

@then(u'close browser')
def close_browser(context):
    context.driver.quit()

