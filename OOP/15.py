class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return f"his name is {self.name} your age {self.age} and his is {self.gender}"
    
    def __repr__(self):
        return f"his name is {self.name} your age {self.age} and his is {self.gender}"   


p1=Person("Eshmat",24,"male")
print(p1)
print(repr(p1))

