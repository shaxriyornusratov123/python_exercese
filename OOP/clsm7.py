class Area:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"{self.x}, {self.y}"

    @classmethod
    def get_square(cls,val):
        return cls(val,val)
    
a1=Area(6,5)
a2=Area.get_square(6)
print(a1)
print(a2)