class Car:
    def __init__(self,engine_number ,mileage):
        self.__engine_number=engine_number
        self.__mileage=mileage

    def print_eng_number(self):
        print( f"{self.__engine_number}")
        print (f"{self.__mileage}")
c=Car("70Z777ZZZ",50000)
c.print_eng_number()
