class Father:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Dauther(Father):
    def __init__(self, name, age,job):
        Father.__init__(name)
        self.job=job
        super().__init__(name, age)


a=Dauther(
    name="gulchapchap",
    age=20,
    job="designer"
)
print(a)