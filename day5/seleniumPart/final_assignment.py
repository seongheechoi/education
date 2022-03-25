from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

url = 'http://www.jolse.com/'
driver.get(url)
time.sleep(2)

skincare = driver.find_element(By.CLASS_NAME, 'main-quick-skin')
# print(skincare)
skincare.click()
time.sleep(2)

tonermist = driver.find_element(By.CLASS_NAME, 'menuCategory').find_elements(By.TAG_NAME, 'li')[9]
tonermist.click()
time.sleep(2)

def printItemInfo(name, price):
    print(name + ', ' + price)

def getItemsInfo(url):
    driver.get(url)
    html = driver.page_source
    bsObj = BeautifulSoup(html, 'html.parser')
    items_info = bsObj.find('div', {'class':'xans-element- xans-product xans-product-normalpackage'})
    items_info = items_info.select('div.description')
    for item in items_info:
        name = item.select('strong.name > a > span')[1].text
        price = item.select('ul > li > span')[0].text
        # print(name+', '+price)
        printItemInfo(name, price)

base_url = driver.current_url
pages = 5

for page in range(1, pages+1):
    url = base_url+'?page='+str(page)
    getItemsInfo(url)

time.sleep(2)
driver.quit()