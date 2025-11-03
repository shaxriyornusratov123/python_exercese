class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

p1=Employee(
    name="eshmat",
    age=19
)

print(p1.name)

