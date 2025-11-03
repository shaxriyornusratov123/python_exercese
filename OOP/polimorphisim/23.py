class Flayer:
    def move(self):
        print("fas")

class Swimmer:
    def move(self):
        print("assdf")

class Goose(Flayer,Swimmer):
    pass

g=Goose()
g.move()

print(Goose.mro())