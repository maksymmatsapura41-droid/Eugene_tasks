import numpy as np

arr = np.array([[1, 2], [3, 4]])

for row in arr:
    print(row, end=' ')

for x in np.nditer(arr):
    print(x, end=' ')
# Output: 1 2 3 4


for x in np.nditer(arr, order='F'):
    print(x, end=' ')
# Output: 1 3 2 4


arr = np.array([1, 2, 3])

# Set flag to 'readwrite' or 'writeonly'
for x in np.nditer(arr, op_flags=['readwrite']):
    x[...] = x * 2

print(arr) # Output: [2, 4, 6]


arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['float64']):
    print(x)


a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20]) # Shape (2,) will be broadcast to (2, 2)

for x, y in np.nditer([a, b]):
    print(f"{x} + {y} = {x + y}")