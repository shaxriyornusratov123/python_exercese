class Animal:
    # def __init__(self,name,color):
    #     self.name=name
    #     self.color=color
    pass
class Mammal(Animal):
    pass 

class Dog(Mammal):
    pass
dog=Dog()
print(issubclass(Mammal,Animal))
print(issubclass(Animal,object))
print(isinstance(dog,Dog))