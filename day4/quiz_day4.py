import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'rucT1vP2bZKUWZL32EOs9REEzut3iz8HQDSwRU1GHIcWQ09VH9XFEl6Y1TUqqLPqPhP6lUJWXBOxK1xLV1JwwQ%3D%3D'

Q0 = quote_plus('서울특별시')
ORD = 'NAME'
pageNo = '1'
numOfRows = '5000'
parameter = 'serviceKey='+serviceKey+'&Q0='+Q0+'&ORD='+ORD+'&pageNo='+pageNo+'&numOfRows='+numOfRows
url = endpoint + parameter
# print(url)

result =requests.get(url)
bsObj = BeautifulSoup(result.content, 'lxml')
items = bsObj.findAll('item')
over_list = []
for item in bsObj.findAll('dutytime1c'):
    print(item.text)
    if int(item.text) > 2100:
        over_list.append(item.text)
print(over_list)
print('월요일 오후9시 초과까지 운영하는 약국의 수 : ', len(over_list), '개')