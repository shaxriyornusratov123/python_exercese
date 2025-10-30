class Student:
    school="greenwood high"
    def __init__(self,name,age):
        self.name=name
        self.age=age

st1=Student("ehsmat",19)
st2=Student("toshmat",18)
print(st1.school)
print(st2.school)

