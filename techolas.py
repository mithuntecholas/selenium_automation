from selenium import webdriver
import time
from selenium.webdriver.common.by import By
actual_title="nopCommerce administration"
Admin_email="admin@yourstore.com"
Admin_password="admin"
driver=webdriver.Chrome()
driver.get(" https://admin-demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)
username=driver.find_element(by=By.ID,value='Email')
password=driver.find_element(by=By.ID,value='Password')
username.clear()
password.clear()
time.sleep(1)
username.send_keys(Admin_email)
time.sleep(1)
password.send_keys(Admin_password)
time.sleep(1)
login=driver.find_element(by=By.CSS_SELECTOR,value="button[type=submit]")
login.click()
captured_title=driver.title
if captured_title==actual_title:
    print("test passed")
else:
    print("test failed")

time.sleep(2)
driver.close()