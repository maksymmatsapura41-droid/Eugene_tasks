class A:
    def process(self): print("A")

class B(A):
    def process(self): print("B")

class C(A):
    def process(self): print("C")

class D(B, C):
    def process(self): print("D")

d = D()
d.process()  # what will be printed
print(D.mro()) # MRO (Method Resolution Order).
