import time

import requests
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://www.orangehrm.com/")
d.maximize_window()
# click_button=d.find_element(By.XPATH,'//*[@id="add-to-cart-button"]')
# click_button.click()
page_links=d.find_elements(By.TAG_NAME,'a')
print(len(page_links))
for link in page_links:
    url=link.get_attribute("href")
    #print(url)
    if url.startswith("https:/"):
        try:
            res=requests.head(url)
            if res.status_code>=400:
                print("broken link",url)
        except:
            print("error")
d.quit()

