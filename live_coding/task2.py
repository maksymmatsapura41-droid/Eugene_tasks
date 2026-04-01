import functools
import time


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return result
    return wrapper

@time_it
def slow_operation():
    total = 0
    for i in range(100_000_000):
        total += i
    return total

slow_operation()
print(slow_operation.__name__)