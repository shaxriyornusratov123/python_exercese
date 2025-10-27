class Movie:
    def __init__(self,title:str,year:int,genre:str)->None:
        self.title=title
        self.year=year
        self.genre=genre

    def info(self):
        return f"title:{self.title},genre:{self.genre},year:{self.year}\n"
    
movie1=Movie("qasoskorlar","scinefiction",2000)
movie2=Movie("sehirli qalpoqcha","comedia",2014)
print(movie1.info())
print(movie2.info())






