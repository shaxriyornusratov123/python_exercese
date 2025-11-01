class Device:
    def __init__(self,name,model,brand):
        self.name=name
        self.model=model
        self.brand=brand
    def status(self):
        print("awenfa")

class Phone(Device):
    def status(self):
        return f"{self.name}"
    
class Laptop(Device):
    def status(self):
        return f"{self.name}"
    
p1=Phone(
    name="iphone",
    model="17 pro max",
    brand="apple"
)
print(p1.status())