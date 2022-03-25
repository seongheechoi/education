from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.naver.com'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

ul_tag = bsObj.find('ul', {'class':'list_nav type_fix'})
print(ul_tag)

for li in ul_tag.findAll('li'):
    a_tag = li.find('a')
    print(a_tag.text)