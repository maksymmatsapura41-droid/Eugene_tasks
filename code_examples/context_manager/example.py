class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Підключення до бази {self.db_name}...")
        # Повертаємо об'єкт, з яким будемо працювати
        return f"З'єднання_з_{self.db_name}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type: тип помилки (наприклад, ValueError)
        # exc_val: об'єкт помилки
        # exc_tb: traceback (шлях помилки)

        print(f" Закриття підключення до {self.db_name}")

        if exc_type:
            print(f"Сталася помилка: {exc_val}")
            # Якщо повернути True, помилка "поглинеться" і не піде далі
            # Якщо False (дефолт), помилка прокинеться вгору
            return False


with DatabaseConnection("Users_DB") as db:
    print(f"Виконую запити через {db}")
    # raise ValueError("Ой, щось пішло не так")