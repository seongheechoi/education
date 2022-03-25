import numpy as np

data1 = [6,7,8,1.5, 2]
print(data1)
print(type(data1))

arr1 = np.array(data1, dtype=np.int32)
print(arr1)
print(type(arr1))
print()

data2 = [[1,2,3],[4,5,6]]
print(data2)
print()
arr2 = np.array(data2)
print(arr2)
print()
print(arr2.shape)
print(arr2.dtype)
print()

arr3 = np.arange(10)
print(arr3)

arr4 = np.linspace(-3, 3, 10)
print(arr4)
print()

arr5 = np.ones([3,4])
print(arr5)

# arr6 = np.zeros([3,4])
# print(arr6)

arr7 = np.empty([3,4])
print(arr7)
