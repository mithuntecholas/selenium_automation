import time

from selenium import  webdriver
from selenium.webdriver.support.select import Select
d=webdriver.Chrome()
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://www.orangehrm.com/contact-sales/")
d.maximize_window()
# selectt=d.find_element(by=By.XPATH,value="//select[@id='Form_submitForm_Country']")
# select_dd=Select(selectt)
# all_counties=select_dd.options
# for country in all_counties:
#     if country.text=="India":
#         country.click()
time.sleep(2)


options=d.find_elements(by=By.XPATH,value="//li[@class='iti__country iti__standard']")
print(len(options))
for op in options:
    #print(op.get_attribute('data-dial-code'))
    if op.get_attribute('data-dial-code').strip()=='91':
        print("comimg inside")
        print(op.get_attribute("data-country-code"))
        if op.is_enabled() :
            print(op)
            op.click()
            break
        else:
            print("not able to click")


time.sleep(2)
#select_dd.select_by_value("India")
# select_dd.select_by_index(12)
#select_dd.select_by_visible_text("India")

d.quit()

