class A:
    def action(self):
        print("acting a")

class B(A):
    def action(self):
        super().action()
        print("acting from b")

class C(A):
    def action(self):
        super().action()
        print("acting from c")

class D(B,C):
    def action(self):
        super().action()
        print("acting from d")
        
d=D()
d.action()
print(D.__mro__)