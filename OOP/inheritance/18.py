class Employee:
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
        
    def describe(self):
        print("anything")
class Manager(Employee):
    def __init__(self):
        super().__init__()

    def describe(self):
        print("manager")

a=Manager()
a.describe