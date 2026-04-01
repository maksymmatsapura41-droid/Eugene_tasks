# Task 1
import asyncio
import random

async def fetch(i):
    await asyncio.sleep(random.random())
    print(f"Fetched {i}")

async def main():
    for i in range(5):
        await fetch(i)

asyncio.run(main())

# Task 2
# @time_it
def slow_operation():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

result = slow_operation()
print("Result:", result)

# Task 3
# @cache
def slow_add(a, b):
    print("Computing...")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))
print(slow_add(4, 5))
print(slow_add(2, 3))


# Task 4
functions = []

for n in range(1, 6):
    functions.append(lambda: n * n)

for func in functions:
    print(func())

# Task5

# Умова:
# Дано список рядків (слів). Написати функцію, яка згрупує слова, що є анаграмами одне одного.
# Анаграми - це слова, які складаються з однакових літер у різній послідовності.
#
# Приклад:
#
# Вхід: ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Вихід: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]