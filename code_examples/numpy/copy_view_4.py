import numpy as np

#COPY
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#View
arr_1 = np.array([1, 2, 3, 4, 5])
x_1 = arr_1.view()
arr_1[0] = 42

print(arr_1)
print(x_1)