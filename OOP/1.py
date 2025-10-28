class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f"model: {self.model}, brand: {self.brand}"

malibu= Car (
        brand="chevrolet",
        model="premier"
    )
tarcker= Car(
        brand="chevrolet",
        model="redline"
    )
print(malibu.brand)   