class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary

    def show_salary(self):
        print(f"name:{self.name}-{self._salary}")  

a=Employee(
    name="eshmat",
    salary=12000
)
a.show_salary()
print(a._salary)
    