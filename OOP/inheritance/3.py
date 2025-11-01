class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"name:{self.name} age:{self.age}")

class Employee(Person):
    def __init__(self, name, age,salary):
        self.salary=salary
        super().__init__(name,age)

    def info(self):
        print(f"name:{self.name} age:{self.age}")

emp=Employee("eshmat",24,5000)
emp.info()
