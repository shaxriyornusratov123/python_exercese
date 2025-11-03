class Person:
    def walk(self):
        print("walking .....")


class Dog(Person):
    def  walk(self):
        super().walk()
        print("wolking with dog  ")

s=Dog()
s.walk()

