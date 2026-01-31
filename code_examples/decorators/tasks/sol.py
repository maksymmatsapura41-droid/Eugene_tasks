import json
import time
from functools import wraps

# ---------- retry ----------
def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Спроба {attempt+1} не вдалася: {e}")
                    last_exception = e
                    time.sleep(0.5)
            raise last_exception
        return wrapper
    return decorator

# ---------- to_json ----------
def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False)
    return wrapper

# ---------- from_json ----------
def from_json(func):
    @wraps(func)
    def wrapper(json_str, *args, **kwargs):
        data = json.loads(json_str)
        return func(data, *args, **kwargs)
    return wrapper

# ---------- Тест декораторів ----------

# Тест retry
@retry(times=3)
def risky_action():
    import random
    if random.random() < 0.7:
        raise ValueError("Щось пішло не так!")
    return "Все пройшло успішно!"

print("=== Тест retry ===")
try:
    print(risky_action())
except Exception as e:
    print("Всі спроби не вдалися:", e)

# Тест to_json / from_json
@to_json
def get_data():
    return {"name": "Максим", "age": 25}

@from_json
def print_data(data):
    print(data["name"], data["age"])

print("\n=== Тест to_json / from_json ===")
json_str = get_data()
print(json_str)
print_data(json_str)
