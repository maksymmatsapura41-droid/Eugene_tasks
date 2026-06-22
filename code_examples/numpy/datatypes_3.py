import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr_1 = np.array(['apple', 'banana', 'cherry'])

print(arr_1.dtype)


arr_2 = np.array([1, 2, 3, 4, 44], dtype='S')

print(arr_2)
print(arr_2.dtype)

arr_3 = np.array([1.1, 2.1, 3.1])

newarr = arr_3.astype('i')

print(newarr)
print(newarr.dtype)

# Useful initializations

arr = np.zeros((2,3), dtype='float')
print(arr)

arr = np.ones((2,3), dtype='float')
print(arr)

arr = np.full((5,5), 99, dtype='float')
print(arr)

arr_1 = np.full_like(arr, 4, dtype='int32')
print(arr_1)