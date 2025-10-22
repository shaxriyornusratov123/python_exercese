def conditional(cond):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if cond(*args,**kwargs):
                return func(*args,**kwargs)
            else:
                print ("skipped due to condition")    
            
        return wrapper
    return decorator
@conditional(lambda x,y : x>y)
def myfunc(a,b):
    print(a,b)
myfunc(10,57)
