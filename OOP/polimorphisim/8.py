class Car:
    def drive(self):
        print("driving a car")

class Chair:
    def sit(self):
        print("you can sit")

def start(obj):
    if hasattr(obj,"drive"):
        obj.drive()
    else:
        print("you can not use it ")

car=Car()
chair=Chair()

start(car)
start(chair)