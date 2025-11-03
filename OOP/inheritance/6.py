class Vehicle:
    def __init__(self,name,type,color):
        self.name=name
        self.type=type
        self.color=color

    def move(self):
        print("moving ...")

    def __str__(self):
        return f"{self.name} {self.type} {self.color}"

class Car(Vehicle):
    pass
c=Car(
    name="moshina",
    type="Car",
    color="yellow"

)
print(c)