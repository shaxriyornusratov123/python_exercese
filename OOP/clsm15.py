class Triangle:
    def uchburchak(A,B,C):
        if A+B>C and A+C>B and C+B>A:
            return True
        return False
       
a=Triangle.uchburchak(3,3,5)
print(a)
