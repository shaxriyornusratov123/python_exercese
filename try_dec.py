def safe_call(func):
    def wrapper(*args,**kwargs):
        try:
            func()
        except ZeroDivisionError:
            print("devsion by zero not allowed")
        except Exception as e:
            raise Exception(e)
        
    return wrapper
@safe_call
def my_func():
    raise Exception("nima gap?")
my_func()
