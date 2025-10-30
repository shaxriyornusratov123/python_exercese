class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def newborn(cls,name):
        return cls(name,0)
    
    def __str__(self):
        return f"{self.name}-{self.age}"
p1=Person("javohir" ,11)
baby=Person.newborn("eshmat")
print(p1)
print(baby)