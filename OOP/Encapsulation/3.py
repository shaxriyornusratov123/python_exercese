class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def display_grade(self):
        print(f"{self.name}-{self.grade}")

st1=Student("eshmat",20,97)
st1.display_grade()