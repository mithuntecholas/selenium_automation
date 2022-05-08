import time
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
opt=webdriver.ChromeOptions()
opt.add_argument("__disable_notifications__")

d.get("https://whatmylocation.com/")
d.maximize_window()



d.quit()

