# #---------------------------------------------------------
# # Завдання: знайди баг у функції з аргументом за замовчуванням
# # Прочитай код і поясни, чому результат різний між першим і наступними викликами функції.
# # Потім внеси зміни так, щоб кожен виклик працював незалежно і не “пам’ятав” попередній стан.
# def add_tag(tag, tags=None):
#     if tags is None:
#         tags = []
#     tags.append(tag)
#     return tags
# print(add_tag("python"))
# print(add_tag("django"))
#
# #---------------------------------------------------------
# # Завдання: поясни поведінку lambda у циклі
# # Подивись на код із циклом, який створює список функцій, і поясни, чому всі функції повертають однакове значення.
# # Після пояснення виправ код так, щоб кожна функція повертала “своє” значення з ітерації.
# funcs = []
# for i in range(3):
#     funcs.append(lambda k = i: k)
# print([f() for f in funcs])
#
# #---------------------------------------------------------
# # Завдання: покращи обробку винятків
# # Проаналізуй функцію, де використовується загальний except Exception.
# # Поясни, чому це небезпечно, і перероби обробку винятків так, щоб перехоплювались лише очікувані помилки.
# def parse_int(value):
#     try:
#         return int(value)
#     except (ValueError, TypeError):
#         return value
#     except Exception:
#         return 0
#
#
# #---------------------------------------------------------
# # Завдання: виправ мутацію списку під час ітерації
# # Розбери код, де елементи видаляються зі списку прямо в циклі for.
# # Поясни, чому частина елементів пропускається, і перепиши рішення так, щоб фільтрація працювала коректно.
# nums = [1, 2, 3, 4, 5, 6, 2, 2, 2]
# nums = [value for value in nums if value%2!=0]
# print(nums)
# #---------------------------------------------------------
# # Завдання: розбери багатокритеріальне сортування
# # Поясни, як працює сортування за двома полями (наприклад, за рейтингом і ім’ям).
# # Потім адаптуй код так, щоб сортування імен було case-insensitive (без залежності від регістру літер).
# users = [
#     {"name": "ann", "score": 10},
#     {"name": "Bob", "score": 15},
#     {"name": "alice", "score": 15},
# ]
# print(sorted(users, key=lambda u: (-u["score"], u["name"].lower())))
#
# #---------------------------------------------------------
#
# # Завдання: правильно оброби значення None у словнику
# # Подивись приклад із dict.get(key, default) і поясни різницю між ситуаціями:
# #
# # ключ відсутній,
# # ключ є, але значення None.
# # Після цього реалізуй коректний fallback, який підходить для обох сценаріїв за вимогою.
# data = {"timeout": None}
# timeout = data.get("timeout", 30)
# if timeout is None:
#     timeout = 30
# print(timeout)
#
#
# #---------------------------------------------------------
# # Завдання: поясни проблему shallow copy
# a = {"skills": ["python", "sql"]}
# b = a.copy()
# b["mongo"] = 3
# b["skills"].append("django")
# print(a)
# print(b)
#
#
# #---------------------------------------------------------
# # Завдання: оптимізуй алгоритм пошуку дубліката
# def has_duplicates(nums):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# #---------------------------------------------------------
#
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
    if not isinstance(follower_id, int) or not isinstance(following_id, int):
        return 400, {"error": "Bad Request"}
    # TODO:
    # 1) Validate required fields
    # 2) Disallow self-follow
    # 3) Return existing relation if already exists
    # 4) Otherwise create relation

    if following_id == follower_id:
        return 400, {"error": "You cannot follow yourself"}
    for followings in FOLLOWS:
        if follower_id == followings.follower_id and following_id == followings.following_id:
            return 200, {"status": "already followed"}
    FOLLOWS.append(Follow(follower_id=follower_id, following_id=following_id))
    return 201, {"status": "created"}

print(follow_user({"follower_id": 1, "following_id": 2}))
print(follow_user({"follower_id": 1, "following_id": 2}))
print(follow_user({"follower_id": 1, "following_id": 1}))
print(follow_user({"follower_id": "1", "following_id": 2}))