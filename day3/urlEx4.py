from urllib.request import urlopen
import re

url = 'https://goo.gl/U7mSQl'

html = urlopen(url)
html_content = html.read().decode('utf-8')
aa = re.findall(r'[a-zA-Z0-9]+\*{3}', html_content)
for a in aa:
    print(a)