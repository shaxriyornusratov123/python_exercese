class Book:
    def __init__(self,name,author,year):
        self.name=name
        self.author=author
        self.year=year
        
    def __str__(self):
        return f"Book<name={self.name}, author={self.author},  year={self.year}>"
    
b1=Book("the quick python","kimdir",2000)
b2= Book("5-sinf musiqa" , "Eshmat",2019)

print(b1,b2)