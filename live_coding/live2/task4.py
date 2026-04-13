# Task 4
# Написати генератор chunker(iterable, size), який приймає список
# (або рядок) і повертає його частинами (чанками) заданого розміру size.

def chunker(iterable, size):
    for item in range(0, len(iterable), size):
        yield iterable[item:item+size]

print(list(chunker([1, 2, 3, 4, 5, 6, 7, 8, 9, 69], 3)))
