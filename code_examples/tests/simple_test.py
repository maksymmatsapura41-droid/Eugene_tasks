# calculator.py
def add(a, b):
    return a + b

def test_add_success():
    assert add(2, 3) == 5  # Ми очікуємо, що 2 + 3 буде 5

def test_add_zero():
    assert add(5, 0) == 5

def test_user_is_root(db_connection):
    assert db_connection["user"] == "root"