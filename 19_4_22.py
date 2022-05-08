from selenium import  webdriver
d=webdriver.Chrome()
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
d.get("https://facebook.com/")
d.maximize_window()
time.sleep(3)



# create_new=d.find_element(by=By.CSS_SELECTOR,value='a[data-testid=open-registration-form-button]')
# create_new.click()
user_name=d.find_element(by=By.CSS_SELECTOR,value='input.inputtext[name=email]')
user_name.send_keys("haaai")
time.sleep(2)

# username=d.find_element(by=By.CSS_SELECTOR,value='input#txtUsername')
# password=d.find_element(by=By.CSS_SELECTOR,value='input#txtPassword')
# username.send_keys("Admin")
# time.sleep(1)
# password.send_keys("admin123")
# time.sleep(1)
# login_button=d.find_element(by=By.CSS_SELECTOR,value='input.button')
# login_button.click()

# login_fb=d.find_element(by=By.CSS_SELECTOR,value='button[type=submit]')

time.sleep(2)


time.sleep(2)
d.close()
d.quit()
