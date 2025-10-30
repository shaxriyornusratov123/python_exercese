class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}  {self.age}"
    @classmethod
    def get_dict(cls,d):
        name=d.get("name","berilmagan")
        age=d.get("age",0)
        return cls(name,age)

print(Student.get_dict({"name":"eshmat","age":19}))

