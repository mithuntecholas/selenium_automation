import time
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://jqueryui.com/datepicker/")
d.maximize_window()
frame=d.find_element(By.XPATH,"//*[@id='content']/iframe")
d.switch_to.frame(0)
input_=d.find_element(By.XPATH,"//*[@id='datepicker']")
input_.click()

time.sleep(3)
month="August"
date="25"
year="2022"
months={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,
        "Nobember":11,"December":12}
is_right=True
month_p = d.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
year_p = d.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")

m_our_digit=months.get(month)
m_get_digit=months.get(month_p.text)
year_get=int(year_p.text)
if year_get<int(year) :
    is_right=True
elif year_get==int(year) and m_our_digit>m_get_digit:
    is_right=True
else:
    is_right=False

while True:
    month_p = d.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
    year_p = d.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
    if month_p.text==month and year_p.text==year:
        break
    else:
        right_click= d.find_element(By.XPATH, "//a[@title='Next']")
        prev_click = d.find_element(By.XPATH, " //a[@title='Prev']")
        if is_right:
            right_click.click()
        else:
            prev_click.click()
dates=d.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for d in dates:
    if d.text ==date:
        d.click()
time.sleep(2)

d.quit()

