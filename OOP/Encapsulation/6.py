class Account:
    def __init__(self,name_user,balance=0):
        self.name_user=name_user
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"sizning balansingiz  {self._balance}")


    def balance(self):
        return self._balance
    

a=Account("eshmat",12000)
a.deposit(50000)
print(a.balance())