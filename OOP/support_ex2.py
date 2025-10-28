class Battery:
    def __init__(self,percentage):
        self.history=[]
        self.persentage=percentage
        if percentage>100:
            self.persentage=100
        elif percentage<0:
            self.persentage=0
        self.history.append(f"{self.persentage} boshidagi zaryad")

    def charger(self,time,num):
        if num<0:
            return
        self.persentage+=time*num
        if self.persentage>100:
            self.persentage=100
        self.history.append(f"{time} minut-> {num}%dan zaryadlandi ")

    def play(self,time,num):
        self.persentage-=time*num
        if self.persentage<0:
            print("uynay olmaysiz , telefon uchgan")

        self.history.append(f"{time} minut-> {num}%dan o'ynaldi ")
b=Battery(50)
b.charger(10,5)
b.play(10, 4)
b.charger(10,3)
print(b.persentage)
print(b.history)

