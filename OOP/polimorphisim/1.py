class Cat:
    def sound(self):
        print("miau!")

class Dog:
    def sound(self):
        print("woow!")

class Cow:
    def sound(self):
        print("muu!")

animals=[Cat(),Dog(),Cow()]

for i in animals:
    i.sound()

    