# Завдання: "Менеджер Транзакцій"
# Напиши контекстний менеджер Transaction, який імітує роботу з банківським рахунком.
#
# При ініціалізації приймає об'єкт рахунку (наприклад, словник {"balance": 100}).
#
# В __enter__ створює "копію" балансу.
#
# Якщо всередині with стається помилка — баланс має відкотитися до початкового стану (rollback).
#
# Якщо все пройшло успішно — новий баланс зберігається.
# Через клас та через декоратор

class Transaction:
    def __init__(self, account: dict):
        self.account = account
        self._original_state = None

    def __enter__(self):
        self._original_state = self.account.copy()
        return self.account

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.account.clear()
            self.account.update(self._original_state)
            print("Transaction rolled back")
            return False
        else:
            print("Transaction committed")
            return True
