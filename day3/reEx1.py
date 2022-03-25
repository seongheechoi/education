import re
r1 = re.compile('Hello')
fobj1 = re.search(r1, 'good Hello World')
print(fobj1)
print(fobj1.span())
print(fobj1.group())
print(fobj1.group(0))

print()
fobj2 = re.search(r'Hello', 'good Hello World')
print(fobj2)

print()
fobj3 = re.search('Hello', 'good Hello World')
print(fobj3)

print()
fobj4 = re.match(r'Hello', 'Hello good Hello World')
print(fobj4)

print()
fobj5 = re.findall(r'Hello', 'Hello good Hello World')
print(fobj5)


print()
fobj6 = re.findall(r'a+b*', 'aaaa cc bbb aabb')
print(fobj6)


print()
fobj7 = re.findall(r'^Hello', 'Hello good Hello World')
print(fobj7)

print()
fobj8 = re.findall(r'[0-9]+', 'Hello 2323good Hello 53 4 World')
print(fobj8)

print()
fobj9 = re.findall(r'h{2}', 'Hello 2323hhgood Hello 53 4 dddhhhWorld')
print(fobj9)

print()
fobj9 = re.findall(r'h{2,3}', 'Hello 2323hhgood Hello 53 4 dddhhhWorld')
print(fobj9)

print()
fobj10 = re.findall(r'\d{2,3}-[0-9]{3,4}-[0-9]{4}',
                    'Hello tel:010-7878-8989 Hello 017-683-8888 53 4 02-778-8989dddhhhWorld')
print(fobj10)

fobj11 = re.findall(r'[a-zA-z]+', 'good tel:010-8989-9829 hi Hello')
print(fobj11)

fobj12 = re.findall(r'\w+', 'good tel:010-8989-9829 hi Hello')
print(fobj12)

fobj13 = re.findall(r'\W+', 'good tel:010-8989-9829 hi Hello')
print(fobj13)