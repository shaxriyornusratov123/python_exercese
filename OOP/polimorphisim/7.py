class Car:
    def run(self):
        print("drive")

class Robot:
    def run(self):
        print("both  of them ")

class Athlet:
    def run(self):
        print("run athlet")

def start(obj):
    obj.run()

a=Car()
start(a)