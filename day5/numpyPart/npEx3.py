import numpy as np

# arr1 = np.arange(10)
# print(arr1)
# print(np.sqrt(arr1))
# print()
# print(np.exp(arr1))
# print()
# print(np.cos(arr1))


arr2 = np.array([[2,6,7,3],
                 [7,5,1,3],
                 [0,2,9,8]])
print(arr2)
print('sum:',arr2.sum())
print('mean:',arr2.mean())
print('std:',arr2.std())
print()

print(arr2.mean(axis=0))
print(arr2.mean(axis=1))

print()

arr3 = np.arange(12)
print(arr3)
print()
print(arr3.reshape([4,3]))