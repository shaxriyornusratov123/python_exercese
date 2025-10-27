class Person:
    def __init__(self,age:int,name:str)-> None:
        self.name=name
        self.age=age
    def __str__(self):
        return f"person<name={self.name}\n,age={self.age}>"
p1=Person(
    name="eshmat",
    age=24
)
p2=Person(
    name="toshnat",
    age=26
)
print(p1,p2)