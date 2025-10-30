class Discount:
    def Skidka(price:int,disc:int):
        a=price*(disc/100)
        return a
    
print(Discount.Skidka(400000,70))
