from selenium import  webdriver
d=webdriver.Chrome()
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#d.get("https://www.orangehrm.com/hris-hr-software-demo/")
d.get("https://admin-demo.nopcommerce.com/")
d.maximize_window()
time.sleep(3)

# print("title",d.title)
# print('website adress',d.current_url)
# print('page source code',d.page_source)

# first_name=d.find_element(by=By.XPATH,value="//input[@id='Form_submitForm_FirstName']")
# if first_name.is_displayed() and first_name.is_enabled():
#     first_name.send_keys("mithun")
# else:
#     print("failed,first name not displayed or not enabled")
# time.sleep(2)

check_box=d.find_element(by=By.XPATH,value="//input[@id='RememberMe']")
print("default status",check_box.is_selected())
time.sleep(2)
check_box.click()
time.sleep(1)
print("status after click",check_box.is_selected())
#
# #free_trial=d.find_element(by=By.XPATH,value="//a[normalize-space()='Contact Sales']")
# free_trial=d.find_element(by=By.XPATH,value="//input[@id='linkadd']")
# print("the text of free trial",free_trial.text)
# print("the text ",free_trial.get_attribute("type"))


# logo_image=d.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/img')
# logo_image.click()

# links=d.find_elements(by=By.TAG_NAME,value='a')
# print(len(links))

# footer_area_links=d.find_elements(by=By.XPATH,value="//div[@class='footer__bot']//a")
# print(type(footer_area_links))
#
# contact_sales=d.find_elements(by=By.XPATH,value="//a[normalize-space()='Contact Sales']")
# print(len(contact_sales))
# contact_sales[0].click()

# for node in footer_area_links:
#     print("link:",node.get_attribute("href"))
# time.sleep(2)

# elemnts=d.find_elements(by=By.CLASS_NAME,value='col-sm-2')
# print(len(elemnts))



d.close()
d.quit()
