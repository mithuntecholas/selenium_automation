import time
from selenium import  webdriver
d=webdriver.Chrome()
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://opensource-demo.orangehrmlive.com/")
d.maximize_window()
link=d.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
time.sleep(2)
link.click()
# w_id=d.current_window_handle
# print(w_id)
w_ids=d.window_handles
print(w_ids)
d.switch_to.window(w_ids[1])
click_ele=d.find_element(By.XPATH,"//input[@id='linkadd']")
click_ele.click()
time.sleep(2)
d.switch_to.window(w_ids[0])
time.sleep(2)
d.quit()

