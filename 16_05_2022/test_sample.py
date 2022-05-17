from selenium import  webdriver
from selenium.webdriver.common.by import By
def test_case1(request,setup):
    print("checking case 1")
    driver=request.module.driver
    driver.find_element(by=By.XPATH,value="//input[@title='Search']")

