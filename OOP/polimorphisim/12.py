class Shape:
    def perimetr(self):
        raise NotImplementedError("not implement")
    
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimetr(self):
        return self.a+self.b+self.c
    
class Rectangle(Shape):
    def __init__(self,A,B):
        self.A=A
        self.B=B
    def perimetr(self):
        return 2*(self.A+self.B)
    
t=Triangle(1,2,3)
r=Rectangle(4,6)
print(t.perimetr())
print(r.perimetr())