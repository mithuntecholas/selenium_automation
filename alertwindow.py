import time
from selenium import  webdriver
d=webdriver.Chrome()
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://the-internet.herokuapp.com/javascript_alerts")
button=d.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
button.click()
time.sleep(4)

a_window=d.switch_to.alert
print(a_window.text)
a_window.accept()
#a_window.dismiss()
d.quit()

