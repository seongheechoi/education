from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('./chromedriver')

def search_coffeeBeanStore(result):
    cb_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome(service=s)

    for i in range(1, 30):
        driver.get(cb_url)
        time.sleep(2)
        try:
            driver.execute_script('storePop2(%d)'%i)
            time.sleep(2)
            html = driver.page_source
            bsObj = BeautifulSoup(html, 'html.parser')
            store_name_h2 = bsObj.select('div.store_txt > h2')
            store_name = store_name_h2[0].text
            # print(store_name_h2)
            store_info = bsObj.select('div.store_txt > table.store_table > tbody > tr > td')
            store_address = store_info[2].text
            # store_address = list(store_info[2])[0]
            store_phone = store_info[3].text
            result.append([store_name, store_address, store_phone])

        except:
            continue

result = []
search_coffeeBeanStore(result)
print(result)