class Flayer:
    def __init__(self,height):
        self.height=height
    def Fly(self):
        print("flying")

class Swimmer:
    def __init__(self,depth):
        self.depth=depth
    def Swim(self):
        print("swimming")

class Duck(Flayer,Swimmer):
    def __init__(self, height,depth):
        Flayer.__init__(self,height)
        Swimmer.__init__(self,depth)

d=Duck(100,10)
d.Fly()
d.Swim()


    