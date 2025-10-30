class Game:
    def __init__(self,score,level):
        self.score=score
        self.level=level

    @classmethod
    def settings(cls):
        return cls(12,32)
    def __str__(self):
        return f"{self.score} {self.level}"
    
G1=Game(12,43)
g2=Game.settings()
print(G1)
print(g2)
print(hasattr(g2,"score"))