class Soldier:
    def attack(self):
        print("askarlar hujumga !!!")

class Tank:
    def attack(self):
        print("tankalr hujumga !!!")

class Helicopter:
    def attack(self):
        print("vertalyotlar hujumga !!!")

hujum=[Soldier(),Tank(),Helicopter()]

for a in hujum:
    a.attack()



    