class BankAccaunt:
    def __init__(self,owner,balance):
        self.owner=owner 
        self.balance=balance

    def __str__(self):
        return f"{self.owner}ning kartasida {self.balance} pul bor"
    
a=BankAccaunt("Eshamt","12000$")
print(a)

