import time
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://opensource-demo.orangehrmlive.com/")
d.maximize_window()
time.sleep(2)
click_button=d.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
click_button.click()
window_ids=d.window_handles
d.switch_to.window(window_ids[1])
free_trial=d.find_element(By.XPATH,"//input[@id='linkadd']")
free_trial.click()
d.switch_to.window(window_ids[0])
time.sleep(5)

d.quit()

