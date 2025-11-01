class Dog:
    def action(self):
        print("barks")

class Car:
    def action(self):
        print("drive")

class Robot:
    def action(self):
        print("both  of them ")

objects=[Dog(),Car(),Robot()]
for obj in objects:
    obj.action()
