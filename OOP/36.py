class Cat:
    def __init__(self,name):
        self.name=name
    

    def __str__(self):
        return f"name:{self.name}"


class Dog:
    def __init__(self,name):
        self.name=name
     

c1=Cat("pishak")
d1=Dog("bobik")
print(isinstance(c1,Dog),isinstance(c1,Cat))