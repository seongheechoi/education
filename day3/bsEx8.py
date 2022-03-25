from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon#Early_work')
bsObj = BeautifulSoup(html, 'html.parser')

for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])