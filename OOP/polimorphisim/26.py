class Employee:
    def work(self):
        print("employee working")

class Developer(Employee):
    def work(self):
        print("developer working")


class Manager(Employee):
    def work(self):
        print("manager working")

workers=[Employee(),Developer(),Manager()]
for w in workers:
    w.work()