class Locker:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin

    def open_locker(self,pin):
        if self.__pin==pin:
            print("Locker opened successfully!")
        else:
            print("incorrect pin")
    
a=Locker("eshmat", 1234)
a.open_locker(1234)
a.open_locker(2344)