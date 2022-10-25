from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.taobao.com")

input = driver.find_element(By.ID,'kw')
sleep(5)
input.send_keys("善地")

button = driver.find_element(By.ID,'su')
button.click()
sleep(10)
print("end")

