import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])


arr_1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr_1[1, 1:4])


# Get specific row
print(arr_1[0, :])
# Get specific column
print(arr_1[:, 3])