import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

newarr_over_42 = arr[arr > 42]
print(newarr_over_42)