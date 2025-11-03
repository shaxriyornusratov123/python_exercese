class Student:
    def __init__(self,marks=0):
        self._marks=marks

    def getter(self):
        return f"{self._marks}"
    
    def setter(self,t):
        if 0>t or t>100:
            print("siz notug'ri qiymat berdinggiz")

        else:
            self._marks=t

st1=Student()
st1.setter(100)
print(st1.getter())
print(st1._marks)
