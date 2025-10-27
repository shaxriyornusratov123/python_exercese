class Player:
    def __init__(self,name,score):
        self.name=name 
        self.score=score
    
    def add_score(self,points):
        self.score+=points
        

p1=Player("Eshmat",200)
print(p1.score)
p1.add_score(10)
print(p1.score)
