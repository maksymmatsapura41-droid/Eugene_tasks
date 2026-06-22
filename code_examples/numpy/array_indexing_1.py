import numpy as np
# ndarray
arr = np.array([1, 2, 3, 4])
print(arr)

print(arr[0])
print(arr[2] + arr[3])

arr_1 = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print('2nd element on 1st row: ', arr_1[0, 1])


arr_2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr_2[0, 1, 2])
print(arr_2[0][1][2])

arr_3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr_3[1, -1])