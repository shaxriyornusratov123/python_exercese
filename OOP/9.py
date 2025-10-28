class Laptop:
    def __init__(self,brand:str,ram:str,price:int)->None:
        self.brand=brand
        self.ram=ram
        self.price=price

    def __str__(self):
        return f"brand:{self.brand}, ram:{self.ram},price:{self.price}\n"
    
lap1=Laptop(
    brand="acer",
    ram="32gb",
    price=1200
)
lap2=Laptop(
    brand="HP",
    ram="16gb",
    price=800
)
print(lap1,lap2)

