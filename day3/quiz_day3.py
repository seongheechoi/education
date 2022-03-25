from urllib.request import urlopen
import re

html = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
html_content = str(html.read().decode('utf-8'))
# print(html_content)

data = re.findall(r'(<td class="left"><a href=")(.+)(">)(.+)(</a></td>)', html_content)
print(data)
print(len(data))

for d in data:
    print('url : http://hanbit.co.kr'+str(d[1]))
    print('title : '+str(d[3]))
    print('---')


# cstr5 = re.sub(r'(\{\s*)\"(\w+)\"\:\s*\"(\w+)\"(\s*\})', '<\\2>\\3</\\2>' ,'{ "name": "kim" }')