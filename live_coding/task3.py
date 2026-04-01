
def cache(func):
    dic = {}
    def wrapper(*args, **kwargs):
        print(dic)
        if args in dic:
            return dic[args]
        result = func(*args, **kwargs)
        dic[args] = result
        return result
    return wrapper


@cache
def slow_add(a, b):
    print("Computing...")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))
print(slow_add(4, 5))
print(slow_add(2, 3))