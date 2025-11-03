class Team :
    def __init__(self,num):
        self.num=num

    def __len__(self):
        return len(self.num)
    
    def __str__(self):
        return f"num:{self.num}"

t1=Team(["eshamat","toshmat","gishmat"])
print(len(t1))

