import time
from selenium import  webdriver
d=webdriver.Chrome()
#my_dt=WebDriverWait(d,10,poll_frequency=2,ignored_exceptions=[Exception])
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
d.maximize_window()
#d.switch_to.frame("packageListFrame")
frame_1=d.find_element(By.XPATH,"//iframe[@title='All Packages']")
d.switch_to.frame(frame_1)
frame1_click=d.find_element(By.XPATH,"/html/body/main/ul/li[2]/a")
frame1_click.click()
time.sleep(2)
d.switch_to.default_content()
d.switch_to.frame("packageFrame")
frame2_click=d.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[3]/a")
frame2_click.click()
time.sleep(3)
d.switch_to.default_content()
d.switch_to.frame("classFrame")
frame3_click=d.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[5]/a")
frame3_click.click()
time.sleep(3)
d.quit()

