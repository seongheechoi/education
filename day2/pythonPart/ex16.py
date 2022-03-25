def num_generator():
    yield 0
    yield 1
    yield 2

for i in num_generator():
    print(i)


def CustomRange2(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

for i in CustomRange2(3):
    print(i)

def gEX(datas):
    for str in datas:
        yield str.upper()


foods = ['juice', 'bread', 'steak']
for data in gEX(foods):
    print(data)