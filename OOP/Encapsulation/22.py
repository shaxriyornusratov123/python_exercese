class Temperature:
    def __init__(self,celsius):
        self._celsius=celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def set_celsius(self,degree):
        if degree>-273.15:
            self._celsius=degree

t=Temperature(10)
t.set_celsius=-100


