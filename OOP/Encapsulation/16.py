class Temperature:
    def __init__(self,celsius=0):
        self._celsius=celsius

    def get_farnheit(self):
        return (self._celsius*1.8)+32


    def setter(self,t):
        if t>-273.15:
            self._celsius=t
        else:
            print("temp 273.15 dan kam bula olmaydi")


    def getter(self):
        return self._celsius
    
    
c=Temperature()

c.setter(32)

print(c.getter())
print(c._celsius)
print(c.get_farnheit())

