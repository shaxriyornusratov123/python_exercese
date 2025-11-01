class Warrior:
    def attack(self):
        print("attacking warrior")

class Mage:
    def attack(self):
        print("attacking mage")

class Archer:
    def attack(self):
        print("attacking archer")

for atc in [Warrior(),Mage(),Archer()]:
    atc.attack()