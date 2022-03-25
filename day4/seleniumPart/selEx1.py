from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('../../day5/seleniumPart/chromedriver')

driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')

from selenium.webdriver.common.by import By
import time
time.sleep(1)

driver.find_element(By.ID, 'id').send_keys('next450')
driver.find_element(By.ID, 'pw').send_keys('kdy1023!')
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()