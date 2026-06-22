import numpy as np

arr = np.array([[1,4,2,1,5,1,6],
                [2,3,1,1,0,6,7]])

print(np.min(arr))

print(np.max(arr))

print(np.sum(arr[0]))

print(np.sum(arr))

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))



# Math

math_arr = np.array([1,4,2,1,5,1,6])
math_arr_2 = np.array([1,4,2,1,5,1,6])

print(math_arr * 2)
print(math_arr ** 2)
print(math_arr + math_arr_2)


matrix = np.array([[1, 2],
                   [3, 4]])

# Overall mean
print(np.mean(matrix))          # Output: 2.5

# Column means (1+3)/2 and (2+4)/2
print(np.mean(matrix, axis=0))  # Output: [2.0, 3.0]

# Row means (1+2)/2 and (3+4)/2
print(np.mean(matrix, axis=1))  # Output: [1.5, 3.5]