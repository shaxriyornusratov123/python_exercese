class Appliance:
    def __init__(self,brand):
        self.brand=brand

 


class WashingMAchine(Appliance):
    def __init__(self, brand,capacity):
        self.capacity=capacity
        super().__init__(brand)

    def __str__(self):
        return f"brand:{self.brand}  capacity:{self.capacity}"


w=WashingMAchine(
    brand="LG",
    capacity=98
)

print(w)