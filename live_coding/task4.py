functions = []

for n in range(1, 6):
    functions.append(lambda m = n: m * m)

for func in functions:
    print(func())