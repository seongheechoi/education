'''
data1 = [i for i in range(10)]
print(data1)


data2 = [i for i in range(10) if i % 2 == 0]
print(data2)

data3 = [i if i % 2 == 0 else 100 for i in range(10)]
print(data3)

str1 = "have a good day"
data4 = [[w.lower(), w.upper(), len(w)]for w in str1.split()]
print(data4)

for i, d in enumerate(['kim','lee','choi'], start=2):
    print(i,d)

str2 = 'it is a good day'
data5 = {i:j for i, j in enumerate(str2.split())}
print(data5)
'''

ldata1 = ['kim', 'lee', 'oh']
ldata2 = ['seoul', 'busan', 'incheon']

for d in zip(ldata1, ldata2):
    print(d)

data = {i : d for i, d in enumerate(zip(ldata1, ldata2))}
print(data)
