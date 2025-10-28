class Prime_number:
    def __init__(self,*numbers):
        self.args=numbers

    def is_prime(self,n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            return True
        
    def get_primes(self):
        tub_sonlar=[]
        for num in self.args:
            if self.is_prime(num):
                tub_sonlar.append(num)
        return tub_sonlar
    
    
numbers=[1,2,3,4,5,6,7,8,9,11,17]
sonlar=Prime_number(numbers)
print(sonlar.get_primes())

