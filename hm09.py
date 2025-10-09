# Global Counter Create a global variable count = 0. Write increment() that increases it by 1 each time it’s called.
count=0
def increment():
    global count 
    count+=1
increment()
increment()
print(count)

# Shadowing Practice Define a variable name = "outer". Inside a function, redefine name = "inner". Print both and note the difference.
name= "outher"
def user():
    name ="inner"
    print(name)
user()
print(name)

# Temperature Tracker Use global to keep a running total of temperatures list across multiple function calls.

temp=[]
def addTemp(gradre: float, celsius: str):
    global  temp
    temp.append([gradre, celsius])
addTemp(40, "c")
addTemp(87,"k")
addTemp(45,"f")
print(temp)


# Resetting Globals Create two functions: set_value() and reset_value(). Both modify a global variable differently. Demonstrate the changes.
x=0
def set_value(n):
    global x
    x=n
    print (x)
set_value(10)
set_value(35)
def reset_value():
    global x
    x=0
    print(x)
reset_value()

# Counter with Local State Create a function counter() that defines count = 0 inside it and increments count each time it’s called inside the same execution. Then see what happens if you call counter() multiple times.

def counter():
    count=0
    count+=1
    print(count)
counter()
counter()

# Local Calculation Write a function sum_and_print(a, b) that defines a local variable total, prints it, and verify it’s not accessible outside.
def sum_and_print(a,b):
    total=a+b
    print(total)
sum_and_print(5,8)

#  Basic Nesting Define a function outer() that prints “Outer start”, defines an inner function inner() printing “Inner call”, and then calls it.
def outer():
    print("outer start")
    def inner():
        print("inner call")
    inner()
outer()

# Sum Helper Create a function calculate(a, b) that defines an inner function add() to return the sum, and then prints it.
def calculate(a,b):
    def add():
        return a+b
    result=add()
    print(result)
calculate(5,7)

# Greeting Generator Outer function greet(name) defines inner message() that returns "Hello, <name>!". Outer returns the result of message().
def greet(name):
    def massage():
        print(f"hello, {name}! ")
    return  massage()
greet("eshmat")

# Double Inner Calls Have two nested inner functions, inner1() and inner2(). Each prints something. Call them both inside outer.
def outer():
    def inner1():
        print("hello")
    def inner2():
        print("salom")
    inner1()
    inner2()
outer()

# 15. Inner Returns Inner Have outer() return inner() without parentheses first (returning the function itself), then with parentheses (returning its result). Compare the difference.











# Mathematical Nesting Outer function math_ops(x, y) defines add(), sub(), and mul() inside. Each prints a result. Call all three.
def math_ops(x,y):
    def add():
        print(x+y)
    def sub():
        print(x-y)
    def mul():
        print(x*y)
    add()
    sub()
    mul()
math_ops(18,4)

# 17.  Nested Multiplication Table table(n) defines inner show_row(i) that prints one row. Loop inside outer() to call inner for each i.





# Sum List Inside Function process_list(nums) defines compute_sum() inside and calls it. Return both the list length and sum.

def process_list(nums):
    def compute_sum():
        for i in nums:
            print( len(nums))
        print(sum(nums))
    compute_sum()
process_list([1,2,3,4])


# Outer Returning Multiple Functions Define outer() that returns two inner functions add_one() and add_two(). Store them in variables and call separately.
def outer():
    def add_one(x):
        return x+1
    def add_two(x):
        return x+8
    return add_one,add_two
one,two=outer()
print(one(2))
print(two(7))
