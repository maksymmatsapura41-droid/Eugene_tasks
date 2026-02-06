# lambda arguments: expression
# map() applies a specific function to every item in an iterable and returns the results.
# Syntax: map(function, iterable)
# filter() constructs an iterator from elements of an iterable for which a function returns True.
# Syntax: filter(function, iterable)
square = lambda x: x * x
print(square(5))


f = lambda x: x + 1
f1 = lambda x, y: x + y
f2 = lambda a, b, c: a + b + c

# 1. [5, 2, 9]
# 2. key - set sorting logic
# 3. [-5, -2, -9] <-> [5, 2,9]
# 4. [-9, -5, -2]
# 5. [9, 5, 2]


print(sorted([5, 2, 9], key=lambda x: -x))
nums = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, nums))

hosts = ["app01", "db01", "cache01"]
new = list(map(lambda h: f"{h}.company.local", hosts))


from functools import partial
# macros or alias
log = lambda msg: print("[LOG]", msg)
info = partial(log, "[INFO]")

#sort by second argument
items = [(1, 5), (3, 1), (4, 9)]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)

# map
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))

#if example
nums = [1, 2, 3, 4]
even_odd = list(map(lambda x: "even" if x % 2 == 0 else "odd", nums))
print(even_odd)


# bad example
process = lambda x: (x ** 2 + 1) / 3 if x % 2 else x * 10