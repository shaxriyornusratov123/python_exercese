class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __lt__(self,other):
        return self.grade<other.grade
    
    # def __gt__(self,other):
    #     return self.

    def __le__(self,other):
        return
    
    def __ge__(self,other):
        return 
    
    










    def __str__(self):
        return f"name:{self.name}"
        
st1=Student("eshmat",85)
st2=Student("toshmat",90)
print(st1<st2)



