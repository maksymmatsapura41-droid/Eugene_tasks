class BaseValidator:
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        self.validate(value) # Виклик методу, який перевизначать нащадки
        instance.__dict__[self.name] = value
    def validate(self, value):
        pass

class StringValidator(BaseValidator):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Має бути рядок")

class NumberValidator(BaseValidator):
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Має бути число")


class User:
    name = StringValidator()
    age = NumberValidator()

u = User()
u.age = 20
u.name = 11

print(u.age, u.name)