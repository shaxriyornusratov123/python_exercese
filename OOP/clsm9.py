class Fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    @classmethod
    def cratefruit(cls,data):
        name,color=data

        return cls(name,color)
    
    def __str__(self):
        return f"{self.name} {self.color}"
    
f1=Fruits.cratefruit(["banana","yellow"])

print(f1.name)
print(f1.color)