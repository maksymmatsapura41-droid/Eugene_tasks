class LoggedAttribute:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.protected_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.protected_name, None)

    def __set__(self, instance, value):
        print(f"LOG: field change {self.public_name} to the {value}")
        setattr(instance, self.protected_name, value)

class Product:
    price = LoggedAttribute()
    stock = LoggedAttribute()

p = Product()
p.price = 100
p.stock = 50

