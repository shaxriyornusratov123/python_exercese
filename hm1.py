# Sum of All: Define sum_all(*args) that returns the sum of all arguments passed.
def sum_all(*args):
    return (sum(args))
print(sum_all(1,2,3))

# Multiply All: Write a function multiply_all(*args) that multiplies all numbers passed
def multiply_all(*args1):
    s=1
    for i in args1:
        s*=i
    return(s)
print(multiply_all(2,3,4))

# tudent Info: Define a function student_info(name, age, **details) that prints student information. Example call:
#student_info("Ali", 21, grade="A", country="Uzbekistan")

def student_info(name, age, **details):
    print (name)
    print (age )
    for key,value, in details.items():
        print (key,value)
student_info("eshmat",24 , grade="A",country="Uzbekistan")


# Keyword Override: Write a function describe_pet(animal, name="Unknown"). Call it using both positional and keyword arguments. 
def describe_pet(animal,name):
    print(f"meninf uy hayvonim {animal}")
    print(f"uning ismi {name}")
describe_pet("it","bobby")

# flexible Average: Define a function average(*numbers) that returns the average of any count of numbers. 
def average(*numbers: int)->int:
    s=0
    for i in numbers:
        s=sum(numbers)/len(numbers)
        return s
print (average(1,2,3,4,5,6,7,8,9,10))

# Dictionary Printer: Write a function print_dict(**kwargs) that prints key-value pairs.
def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
print(print_dict(name="eshmat",age=36,ishlaydi="quruvchi"))

# Args & Kwargs Combo: Create a function show_data(*args, **kwargs) that prints args and kwargs separately. 
def show_data(*args,**kwargs):
    print(args)
    print(kwargs)
    return kwargs
print(show_data(7.10 , sana="7chi oktyabr"))


# Sum or Multiply: Write a function calculate(*args, operation="sum") that performs either sum or multiplication depending on the keyword argument.

def calculate(*args,operation="sum"):
    if operation=="sum":
        return(sum(args))
    elif operation=="multiply": 
        
        result=1
        for i in args:
            result*=i
            return result
    else :
        return "notugri operatsiya"
print(calculate(1,2,3, operation="sum"))
print (calculate(1,2,3,4,5,6, operation="multiply"))
calculate(1,2,3, operation="add")

# Configurable Greeting: Define a function custom_greet(name, **options) that can change greeting style:






# Build Sentence: Write a function build_sentence(*words, sep=" ") that joins words with the given separator and returns the sentence.
def build_sentence(*words,sep=" "):
    return sep.join(words)
print(build_sentence("my" , "name","is","eshmat",sep="-"))
