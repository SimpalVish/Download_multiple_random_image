import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32 (1)\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.unrealperson.com/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)","")
i=100
for i in range(100):
    driver.find_element(By.CLASS_NAME, 'p-button-success').click()
    time.sleep(5)
    img = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
    time.sleep(5)

driver.close()