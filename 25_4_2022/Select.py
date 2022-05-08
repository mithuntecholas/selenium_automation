import time
from selenium import  webdriver
from selenium.webdriver.support.select import Select
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
d.maximize_window()
# country=d.find_element(By.XPATH,"//select[@id='Form_submitForm_Country']")
# country_list=Select(country)
# #country_list.select_by_value("India")
# country_list.select_by_visible_text("Australia")


options=d.find_elements(By.XPATH,"//select[@id='Form_submitForm_Country']//option")
print(len(options))

for op in options:
    if op.get_attribute("value")=="India":
        op.click()

time.sleep(3)




d.quit()

