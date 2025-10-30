class Even:
    def is_even(n:int):
        if n%2==0:
            return True
        return False
    
print(Even.is_even(3))
print(vars(Even))
