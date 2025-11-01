class Vehicle:
    def drive(self):
        raise NotImplementedError("nksdfbl")

class Car(Vehicle):
    def drive(self):
        print("driving a car")

class Bike(Vehicle):
    def drive(self):
        print("driving a bike")

for vehic in [Car(),Bike()]:
    vehic.drive()

