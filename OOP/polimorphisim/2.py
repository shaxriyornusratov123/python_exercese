class Cat:
    def sound(self):
        print("miau!")

class Dog:
    def sound(self):
        print("woow!")

class Cow:
    def sound(self):
        print("muu!")

def animal_sound(animal):
    animal.sound()

dog=Dog()
cat=Cat()
cow=Cow()
animal_sound(cat)
animal_sound(dog)
animal_sound(cow)

