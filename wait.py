from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
d=webdriver.Chrome()
from selenium.webdriver.common.by import By
mywait=WebDriverWait(d,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException])
d.get("https://facebook.com/")
d.maximize_window()
user_name=mywait.until(ec.presence_of_element_located((By.XPATH,"//input[@id='email']")))
user_name.send_keys("haaai")
d.quit()
