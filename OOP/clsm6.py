import random
class Color:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

    @classmethod
    def randcolor(cls):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        return cls(r,g,b)
    def __str__(self):
        return f"r:{self.r} g:{self.g} b:{self.b}"
    
c1=Color(1,2,3)
c2=Color.randcolor()
print(c1)
print(c2)

