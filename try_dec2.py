def validate_args(func):
    def wrapper(*args,**kwargs):
        for i in args:
                if not isinstance(i,int):
                        raise TypeError("int emas")
        func(*args)              
    return wrapper 
@validate_args
def myfunc(*args):
      print(args)
myfunc(1,2,3,"sw")
