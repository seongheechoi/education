from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('../../day5/seleniumPart/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.naver.com')
time.sleep(1)

login_btn = driver.find_element(By.CLASS_NAME, 'ico_naver')
login_btn.click()
time.sleep(1)

tag_id = driver.find_element(By.NAME, 'id')
tag_pw = driver.find_element(By.NAME, 'pw')

tag_id.clear()
time.sleep(1)

tag_id.click()

import os
text = 'next450'
os.system("echo '{}' | xclip -selection clipboard".format(text))
from selenium.webdriver.common.keys import Keys
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

tag_pw.click()
tag_pw.send_keys('kdy1023!')
time.sleep(1)

login_btn = driver.find_element(By.ID, 'log.login')
login_btn.click()

from bs4 import BeautifulSoup

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
print(bsObj)