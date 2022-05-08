import time
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
rows=d.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
columns=d.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
print(f"numberof rows : {len(rows)}\n number of rows {len(columns)}")

#finding specific datata from the table
#read all the row and column data
#list the data based on the condition


d.quit()

