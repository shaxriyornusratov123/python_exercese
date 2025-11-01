class A:
    def __init__(self):
        print("a class yaratilmoqda")

class B:
    def __init__(self):
        print("b class yaratilmoqda ")

class C(A,B):
   def __init__(self):
       A.__init__(self)
       B.__init__(self)
  
print(C.__mro__)