class Validator:
    def __init__(self, validation_func):
        self.validation_func = validation_func

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not self.validation_func(value):
            raise ValueError(f"Wrong value for {self.name}: {value}")

        print(f"Writing {self.name} = {value}")
        instance.__dict__[self.name] = value


def is_adult(val): return val >= 18


def is_valid_email(val): return "@" in val and "." in val


def is_positive(val): return val > 0


class User:
    age = Validator(is_adult)
    email = Validator(is_valid_email)
    balance = Validator(is_positive)


u = User()
u.age = 20
u.email = "test@me.com"
# u.balance = -10   # Помилка!