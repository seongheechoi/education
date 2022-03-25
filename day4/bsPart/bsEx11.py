from bs4 import BeautifulSoup
from urllib.request import urlopen

def holly_store(result):
    for page in range(1, 6):
        holly_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store='%page
        # print(holly_url)
        html = urlopen(holly_url)
        bsObj = BeautifulSoup(html, 'html.parser')
        tag_tbody = bsObj.find('tbody')
        for store in tag_tbody.findAll('tr'):
            store_td = store.findAll('td')
            store_name = store_td[1].text
            store_sido = store_td[0].text
            store_address = store_td[3].text
            store_phone = store_td[5].text
            result.append([store_name, store_sido, store_address, store_phone])


result = []
holly_store(result)
for sdata in result:
    print(sdata)
print(len(result))