class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def sound(self):
        print("nimadir")
class Mammal(Animal):
    def __init__(self, name, color,size):
        self.size=size
        super().__init__(name, color)

class Dog(Mammal):
    def __init__(self, name, color, size,barks):
        super().__init__(name, color, size)
        self.barks=barks

d=Dog(
    name="tuzik",
    color="malla",
    size="normal",
    barks=True
)
