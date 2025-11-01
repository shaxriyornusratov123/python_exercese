class Shape:
    def area(self):
        print("area of shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        import math
        return  math.pi*self.radius**2
    
class Square(Shape):
    def __init__(self,width):
        self.width=width
    def area(self):
        return self.width**2

for shape in [Circle(4),Square(5)]:
    print(shape.area())