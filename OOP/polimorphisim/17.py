class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def __str__(self):
        return f"title:{self.title} author:{self.author}"
    

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

b1=Book("harry potter","j.k.rowling")
b2=Book("harry potter","j.k.rowling")
b3=Book("chuqintilgan ota","mario pyuzo")
print(b1==b2)
print(b1==b3)


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __eq__(self, other):
#         if not isinstance(other, Book):
#             return NotImplemented
#         return self.title == other.title and self.author == other.author

# # Sinov
# b1 = Book("1984", "George Orwell")
# b2 = Book("1984", "George Orwell")
# b3 = Book("Animal Farm", "George Orwell")

# print(b1 == b2)  # True
# print(b1 == b3)  # False
