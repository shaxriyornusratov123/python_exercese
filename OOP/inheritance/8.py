class Hero:
    def power(self):
        return "strong.. "

class Spiderman(Hero):
    def power(self):
        return "power of Spiderman"

h=Hero()
s=Spiderman()
print(h.power())
print(s.power())