class Duck:
    def quack(self):
        print("quack duck")

    def walk(self):
        print("walk duck")

class Person:
    def quack(self):
        print("quack person")

    def walk(self):
        print("walk person")

def make_it_quack(obj):
    obj.quack()
    obj.walk()

donald=Duck()
eshmat=Person()

make_it_quack(donald)
make_it_quack(eshmat)