class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    
    def __str__(self):
        return f"{self.name}-{self.age}"

a=Person(
    name="eshmat",
    age=26
)
print(a.name,a.__age)