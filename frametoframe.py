

import time
from selenium import  webdriver
d=webdriver.Chrome()
d.implicitly_wait(10)
from selenium.webdriver.common.by import By
d.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(2)
d.switch_to.frame("packageListFrame")
frame_1_elemet=d.find_element(By.LINK_TEXT,"org.openqa.selenium.chrome")
frame_1_elemet.click()
time.sleep(2)
d.switch_to.default_content()
d.switch_to.frame("packageFrame")
frame_2_element=d.find_element(By.LINK_TEXT,"ChromeDriver")
frame_2_element.click()
time.sleep(2)
d.switch_to.default_content()
d.switch_to.frame("classFrame")
frame_3_element=d.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[4]/a")
frame_3_element.click()
d.quit()

