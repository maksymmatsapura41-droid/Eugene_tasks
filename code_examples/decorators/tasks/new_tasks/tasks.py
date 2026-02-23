# Завдання 1: "Секундомір" (Базовий декоратор)
# Мета: Навчитися працювати з часом та functools.wraps.
# Твоя задача: Напиши декоратор @time_it, який вимірює час виконання функції в секундах і виводить його в консоль.
# Використовуй модуль time.
# Обов'язково збережи метадані оригінальної функції.
# Протестуй на функції, яка "спить" 1.5 секунди за допомогою time.sleep().
import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


@time_it
def sleepy_function():
    time.sleep(1.5)


sleepy_function()

# Завдання 2: "Обмежувач доступу" (Декоратор з аргументами)
# Мета: Опанувати фабрику декораторів (потрійну вкладеність).
# Твоя задача: Напиши декоратор @require_role(role), який перевіряє права користувача перед викликом функції.
# Припустимо, у нас є глобальна змінна CURRENT_USER_ROLE = "guest".
# Декоратор має приймати рядок (наприклад, "admin").
# Якщо роль користувача збігається з ролю в декораторі — функція виконується.
# Якщо ні — декоратор має вивести: AccessDenied: Low permissions (або кинути помилку PermissionError).
CURRENT_USER_ROLE = "guest"


def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_USER_ROLE != role:
                raise PermissionError("AccessDenied: Low permissions")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@require_role("admin")
def delete_user():
    print("User deleted")


try:
    delete_user()
except PermissionError as e:
    print(e)

# Завдання 3: "Розумний Кеш" (Клас-декоратор)
# Мета: Реалізація збереження стану (stateful decorator) через екземпляр класу.
# Твоя задача: Напиши клас-декоратор CacheResult.
# Він повинен зберігати результати попередніх викликів функції у словнику (де ключі — це аргументи *args).
# Якщо функція викликається з тими ж аргументами вдруге — результат має братися зі словника,
# а не обчислюватися знову.

class CacheResult:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print("Returning cached result")
            return self.cache[args]

        print("Computing result")
        result = self.func(*args)
        self.cache[args] = result
        return result

    def clear_cache(self):
        self.cache.clear()
        print("Cache cleared")


@CacheResult
def slow_add(a, b):
    time.sleep(1)
    return a + b


print(slow_add(2, 3))  # обчислюється
print(slow_add(2, 3))  # береться з кешу

slow_add.clear_cache()
print(slow_add(2, 3))  # знову обчислюється

# Додай метод .clear_cache(), щоб можна було скинути історію.
# Завдання 4: "Retry Policy" (Комбіноване завдання)
# Мета: Створення складного інструменту для стабільності коду.
# Твоя задача: Напиши декоратор @retry(times=3, delay=1).
# Він має перехоплювати будь-які виключення (Exception) під час виконання функції.
# Якщо сталася помилка, він чекає delay секунд і пробує знову (максимум times разів).
# Якщо після всіх спроб функція так і не запрацювала — прокинь помилку далі.

