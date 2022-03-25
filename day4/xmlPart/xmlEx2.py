import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'rucT1vP2bZKUWZL32EOs9REEzut3iz8HQDSwRU1GHIcWQ09VH9XFEl6Y1TUqqLPqPhP6lUJWXBOxK1xLV1JwwQ%3D%3D'

Q0 = quote_plus('서울특별시')
print(Q0)
Q1 = quote_plus('강남')
QN = quote_plus('삼성약국')
QT = '4'
ORD = 'NAME'
pageNo = '1'
numOfRows = '10'
parameter = 'serviceKey='+serviceKey+'&Q0='+Q0+'&Q1='+Q1+'&QN='+QN+'&ORD='+ORD+'&pageNo='+pageNo+'&numOfRows='+numOfRows
url = endpoint + parameter
print(url)

result =requests.get(url)
bsObj = BeautifulSoup(result.content, 'lxml')
items = bsObj.findAll('item')
for item in bsObj.findAll('dutyname'):
    print(item.text)