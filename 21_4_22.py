from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotInteractableException
d=webdriver.Chrome()
my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
# d.implicitly_wait()
from selenium.webdriver.common.by import By
d.get("https://www.orangehrm.com/")
d.maximize_window()
# privacy_button=d.find_element(by=By.XPATH,value="//a[normalize-space()='Privacy Policy']")

free_trial_button=my_dt.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='linkadd']")))
free_trial_button.click()
d.quit()

