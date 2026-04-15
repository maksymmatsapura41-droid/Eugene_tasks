#---------------------------------------------------------
# Завдання: знайди баг у функції з аргументом за замовчуванням
# Прочитай код і поясни, чому результат різний між першим і наступними викликами функції.
# Потім внеси зміни так, щоб кожен виклик працював незалежно і не “пам’ятав” попередній стан.
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags
print(add_tag("python"))
print(add_tag("django"))

#---------------------------------------------------------
# Завдання: поясни поведінку lambda у циклі
# Подивись на код із циклом, який створює список функцій, і поясни, чому всі функції повертають однакове значення.
# Після пояснення виправ код так, щоб кожна функція повертала “своє” значення з ітерації.
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])

#---------------------------------------------------------
# Завдання: покращи обробку винятків
# Проаналізуй функцію, де використовується загальний except Exception.
# Поясни, чому це небезпечно, і перероби обробку винятків так, щоб перехоплювались лише очікувані помилки.
def parse_int(value):
    try:
        return int(value)
    except Exception:
        return 0


#---------------------------------------------------------
# Завдання: виправ мутацію списку під час ітерації
# Розбери код, де елементи видаляються зі списку прямо в циклі for.
# Поясни, чому частина елементів пропускається, і перепиши рішення так, щоб фільтрація працювала коректно.
nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
#---------------------------------------------------------
# Завдання: розбери багатокритеріальне сортування
# Поясни, як працює сортування за двома полями (наприклад, за рейтингом і ім’ям).
# Потім адаптуй код так, щоб сортування імен було case-insensitive (без залежності від регістру літер).
users = [
    {"name": "ann", "score": 10},
    {"name": "Bob", "score": 15},
    {"name": "alice", "score": 15},
]
print(sorted(users, key=lambda u: (-u["score"], u["name"])))

#---------------------------------------------------------

# Завдання: правильно оброби значення None у словнику
# Подивись приклад із dict.get(key, default) і поясни різницю між ситуаціями:
#
# ключ відсутній,
# ключ є, але значення None.
# Після цього реалізуй коректний fallback, який підходить для обох сценаріїв за вимогою.
data = {"timeout": None}
timeout = data.get("timeout", 30)
print(timeout)


#---------------------------------------------------------
# Завдання: поясни проблему shallow copy
a = {"skills": ["python", "sql"]}
b = a.copy()
b["skills"].append("django")
print(a)
print(b)


#---------------------------------------------------------
# Завдання: оптимізуй алгоритм пошуку дубліката
def has_duplicates(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Use set as unique elements
#---------------------------------------------------------

# Реалізуй endpoint POST /follow, який приймає follower_id і following_id.
#
# Вимоги:
#
# Не можна підписатись на самого себе.
# Якщо підписка вже існує - не створювати дубль, повернути "already_following".
# Якщо не існує - створити і повернути "created".


from dataclasses import dataclass

@dataclass
class Follow:
    follower_id: int
    following_id: int


FOLLOWS: list[Follow] = []


def follow_user(payload: dict) -> tuple[int, dict]:
    """
    Simulates POST /follow
    Input payload example: {"follower_id": 1, "following_id": 2}
    Returns: (status_code, response_json)
    """
    follower_id = payload.get("follower_id")
    following_id = payload.get("following_id")

    # TODO:
    # 1) Validate required fields
    # 2) Disallow self-follow
    # 3) Return existing relation if already exists
    # 4) Otherwise create relation

    FOLLOWS.append(Follow(follower_id=follower_id, following_id=following_id))
    return 201, {"status": "created"}



#-----------------------------------------------------------------------------
#Завдання: чому другий list порожній? Як зробити “багаторазовий” прохід без подвійної роботи?
xs = map(str.upper, ["a", "b"])
print(list(xs))
print(list(xs))


#------------------------------------------------------------------------------
# Завдання: що поверне список і чому?
def make_handlers():
    hs = []
    for i in range(3):
        def h():
            return i
        hs.append(h)
    return hs
[f() for f in make_handlers()]

#--------------------------------------------------------------------------------
#Завдання: що станеться і чому?
def f(a, b, c=0):
    return a + b + c
args = (1, 2)
kwargs = {"c": 3, "b": 4}
print(f(*args, **kwargs))

#-------------------------------------------------------------------------------
#Завдання: який класичний баг та як виправити?
from dataclasses import dataclass
@dataclass
class Box:
    items: list[int] = []

#-----------------------------------------------------------------------------------
#Завдання: чому це небезпечно? Як ітерувати “без зміни під ногами”?
lines = ["a", "b", "c"]
for i, line in enumerate(lines, start=1):
    if line == "b":
        del lines[i]


#------------------------------------------------------------------------------------
# Завдання: що поверне f()
def f():
    try:
        return 1
    finally:
        return 2


#-----------------------------------------------------------------------------------
# Завдання: що втрачається? Виправ декоратор.
def deco(fn):
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper

@deco
def add(x, y):
    """adds"""
    return x + y

print(add.__name__, add.__doc__)
