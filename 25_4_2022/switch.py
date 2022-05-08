import time
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://the-internet.herokuapp.com/javascript_alerts")
d.maximize_window()
click_button=d.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
click_button.click()

alert_w=d.switch_to.alert
time.sleep(2)
#alert_w.accept()
print(alert_w.text)
alert_w.send_keys("haaaiiiiiiiiiiiiiiiiiiiiiiiii")
time.sleep(2)
alert_w.dismiss()

d.quit()

