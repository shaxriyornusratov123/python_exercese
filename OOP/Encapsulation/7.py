class BankAccount:
    def __init__(self,name,age,jshshir,balance):
        self.name=name
        self.age=age
        self.jshshir=jshshir
        self.__balance=balance

    def get_balance(self):
        return f"{self.__balance}"


    def change_balance(self,new_balance):
        self.__balance=new_balance

a=BankAccount(
    name="toshmat",
    age=24,
    jshshir=123456789101212,
    balance=120000000
)

print(a.name,a.age,a.jshshir,a._BankAccount__balance)

print(a.get_balance())