class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def __str__(self):
        return f"name:{self.name},aothor:{self.author}"

    @classmethod
    def default_create(cls):
        return Book("unknown","unknown")
    3
b1=Book("kdald","'psijf")
print(Book.default_create())