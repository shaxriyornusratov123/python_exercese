class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"x={self.x}, y={self.y}"

    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
a1=Point(5,6)
a2=Point(2,1)
print(a1-a2)