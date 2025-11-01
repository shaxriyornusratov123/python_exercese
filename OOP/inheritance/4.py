import math

class Shape:

    def Area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def Area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return self.radius**2*math.pi
    
rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rect.Area()}")
print(f"Circle area: {circle.Area()}")

