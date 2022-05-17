from selenium.webdriver.common.by import By
import time



def test_case1(request,setup):
    driver=request.module.driver
    print("tesing  case 1")
    search_box=driver.find_element(By.XPATH,"//input[@title='Search']")
    time.sleep(3)
    search_box.send_keys("haaiii")

