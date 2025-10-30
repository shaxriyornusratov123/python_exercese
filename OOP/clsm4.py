class Circle:
    def __init__(self,radius):
        self.radius=radius

    @classmethod
    def dmtr(cls,diametr):
        return Circle(radius=diametr/2)
    def __repr__(self):
        return f"circle<r={self.radius}>"
    
    @staticmethod
    def is_even(n:int):
        return n%2==0

c1=Circle.dmtr(10)
print(Circle.is_even(4))
print(c1)