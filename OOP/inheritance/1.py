class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "nimadir"
    
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "miau!"
