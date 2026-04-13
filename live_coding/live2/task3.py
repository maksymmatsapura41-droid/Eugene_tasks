# Task 3
# Написати декоратор @retry(n), який змушує функцію повторити спробу виконання,
# якщо вона викликала виняток (Exception).
# Декоратор має зробити максимум n спроб. Якщо всі n спроб невдалі - прокинути виняток далі.

def retry(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except:
                    print(f"Retrying {i+1}")
                    if i == n-1:
                        raise
        return wrapper
    return decorator


@retry(10)
def dovbo():
    raise ValueError

dovbo()