class ValidAge:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            print("aa")
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be >= 0!")
        print(f"Refreshing {self.name} to {value}")
        instance.__dict__[self.name] = value

class User:
    age = ValidAge('age')
    name = ValidAge('name')

u = User()
u.age = 25
print(u.age)

u.name = "test"
print(u.name)