class Phone:
    def __init__(self,name,color,brand):
        self.name=name
        self.color=color
        self.brand=brand

class SmartPhone(Phone):
    def __init__(self, name, color, brand,camera):
        super().__init__(name, color, brand)
        self.camera=camera
        print(f"{self.camera}")
    
    def __str__(self):
        return f"{self.name},{self.color},{self.brand}"

s=SmartPhone(
    name="iphone",
    color="white",
    brand="apple",
    camera=1000
)


print(s)


