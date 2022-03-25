from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

searchStr = input('찾을 이미지 이름:')
baseUrl = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
url = baseUrl + quote_plus(searchStr)
print(url)

s = Service('../../day5/seleniumPart/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get(url)
time.sleep(5)

html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')

thumnails = bsObj.select('#imgList > div > a > img')

import dload

for thumnail in thumnails:
    src = thumnail['src']
    print(src)
    rvar = str(round(random.random()*1000000))
    dload.save(src, f'imgs/{searchStr}{rvar}.jpg')

driver.quit()
