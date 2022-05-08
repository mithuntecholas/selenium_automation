from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 1st method
# from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://www.google.com")
# time.sleep(3)
# driver.close()

driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

search_box=driver.find_element(by=By.NAME,value='q')
search_box.send_keys("techolas")

time.sleep(2)

search_button=driver.find_element(by=By.NAME,value='btnK')
search_button.click()
time.sleep(2)
driver.close()
