from bs4 import BeautifulSoup

html_str = '''
<html>
    <body>
        <ul class='ok'>
            <li>
                <a href='https://www.daum.net'>다음</a>
            </li>
            <li>
                <a href='https://www.naver.com'>네이버</a>
            </li>
        </ul>
        <ul class='fsite'>
            <li>
                <a href='https://www.google.com'>구글</a>
            </li>
            <li>
                <a href='https://www.facebook.com'>페이스북</a>
            </li>
        </ul>
    </body>
</html?
'''

bsObj = BeautifulSoup(html_str, 'html.parser')
atag = bsObj.find('a')
# print(atag)
# print(atag['href'])

atags = bsObj.findAll('a')
print(atags)
print([(a['href'], a.text) for a in atags])
# print([a.text for a in atags])