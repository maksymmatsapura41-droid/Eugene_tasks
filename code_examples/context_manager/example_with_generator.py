from contextlib import contextmanager

@contextmanager
def temporary_file_setup(filename):
    # Код до yield — це аналог __enter__
    print(f"Створюємо файл {filename}")
    f = open(filename, "w")
    try:
        yield f  # Повертаємо об'єкт у блок with
    finally:
        # Код після yield (в блоці finally) — це аналог __exit__
        print(f"Видаляємо/Закриваємо файл {filename}")
        f.close()

with temporary_file_setup("test.txt") as f:
    f.write("Привіт, Python!")