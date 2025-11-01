class Vehicle:
    def __init__(self,name,color,brand):
        self.name=name
        self.color=color
        self.brand=brand

    def move(self):
        print("moving...")

class Plane(Vehicle):
    def move(self):
        print("flying...")

class Aircraft(Plane):
    def __init__(self, name, color, brand,weapon_capacity, target_accuracy):
        self.weapon_capacity=weapon_capacity
        self.target_accurancy=target_accuracy
        super().__init__(name, color, brand)


    def bomb(self):
        print("bombing...")

v=Vehicle(
    name="asd",
    color="white",
    brand="kedf"
)

p=Plane(
    name="boeing",
    color="red",
    brand="boeing"
)

a=Aircraft(
    name="f16",
    color="black",
    brand=";ksdf",
    weapon_capacity=10000,
    target_accuracy=99
)
print(v.__class__.__name__)
print(p.__class__.__name__)
print(a.__class__.__name__)
