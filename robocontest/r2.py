def find_nod_subtraction(a, b,c,d):
    while a**b-c!= d:
        if a**b-c!= d:
            a**b-c= (a**b-c)-d
        else:
            b = b - a
    return a

num1 = 48
num2 = 18
print(f"НОД({num1}, {num2}) = {find_nod_subtraction(num1, num2)}")
