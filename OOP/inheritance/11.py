class Bird:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print("flying...")

class Parrot(Bird):
    def __init__(self, name):
        super().fly()
        super().__init__(name)

p=Parrot(
    name="qush"
)
print(p.name)