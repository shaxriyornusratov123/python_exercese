class UserAccount:
    def __init__(self,password=0):
        self._password=password

    def set_password(self,pin):
        self._password=pin
    
    def check_password(self):
        return f"{self._password}"
    
user=UserAccount()
user.set_password(1234)
print(user.check_password())


