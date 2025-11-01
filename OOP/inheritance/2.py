class Vehicle:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def move(self):
        print("vehilce moving...")
    
class Car(Vehicle):
    def move(self):
        print("vuuuuuuum...")


class Boat(Vehicle):
    def move(self):
        print("shrrrrrrr...")

