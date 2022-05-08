import requests
from selenium import  webdriver
d=webdriver.Chrome()
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://www.orangehrm.com/")
d.maximize_window()
links=d.find_elements(by=By.TAG_NAME,value='a')
print("broken codes:")
good_links=[]
for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
        if res.status_code >= 400:
            print(url)
        else:
            good_links.append(url)
    except:
        None


d.quit()

