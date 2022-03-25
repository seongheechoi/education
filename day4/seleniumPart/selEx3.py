from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('../../day5/seleniumPart/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.naver.com')

input_element = driver.find_element(By.NAME, 'query')
input_element.send_keys("python")
input_element.send_keys(Keys.RETURN)

from bs4 import BeautifulSoup

html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')

tag = bsObj.select('ul > li > a')
for i in tag:
    print(i)