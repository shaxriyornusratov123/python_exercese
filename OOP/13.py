import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance_from_origin(self):
        return math.sqrt(self.x**2+self.y**2)

cor1=Point(5,12)
print(cor1.distance_from_origin())

