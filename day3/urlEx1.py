from urllib.request import urlopen

uf2 = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
#print(uf2.read())

encoding = uf2.info().get_content_charset(failobj='utf-8')
#print(encoding)

text = uf2.read().decode(encoding)
print(text)