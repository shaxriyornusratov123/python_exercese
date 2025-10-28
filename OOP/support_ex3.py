class Product:
    def __init__(self,name,cost,stock):
        self.name=name
        self.cost=cost
        self.stock=stock

    def add(self,amount):
        self.stock+=amount



    def cell(self,amount):
        self.stock-=amount
        if self.stock<=0:
            print("bu maxsulot qolmagan")
        
a=Product(
    name="kartoshka",
    cost=5000,
    stock=500
)
a.add(10)
a.cell(100)
print(a.stock)
