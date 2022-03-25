from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
url = 'http://search.danawa.com/dsearch.php?k1=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&module=goods&act=dispMain'
driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item')
# print(prod_items)

title = prod_items[1].select('p.prod_name > a')[0].text.strip()
# print(title)

spec_list = prod_items[1].select('div.spec_list')[0].text.strip()
# print(spec_list)

price = prod_items[1].select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',', '')
# print(price)

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title = ''
        try:
            spec_list = prod_item.select('div.spec_list')[0].text.strip()
        except:
            spec_list = ''
        try:
            price = prod_item.select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
        except:
            price = ''
        prod_data.append([title, spec_list, price])
    return prod_data

prod_data = get_prod_items(prod_items)

print(prod_data)

driver.quit()