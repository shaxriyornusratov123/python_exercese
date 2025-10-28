class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.heihgt=height

    def __repr__(self):
        return f"width: {self.width}, height: {self.heihgt}"
    
a=Rectangle(4,5)
print(repr(a))