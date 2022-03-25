# def f1(x):
#     return x ** 2
# print(f1(10))
#
# f2 = lambda x: x**2
# print(f2(10))
#
# def calc(cf, a, b):
#     result = cf(a,b)
#     print(result)
#
# calc(lambda x, y: x * y, 100, 200)

# idata = input('두 정수 값을 읿력하세요')
# print(list(map(int, idata.split())))
#
# val1, val2 = list(map(lambda x : int(x) * 100, idata.split()))
# print(val1, val2)
# print(val1 + val2)

ldata = [4,9,0,1,7,5,6]
ldata.sort()
print(ldata)

ldata2 = [('kim', 88), ('lee', 90), ('choi', 92), ('oh', 77)]
ldata2.sort(key= lambda x : x[1])
print(ldata2)