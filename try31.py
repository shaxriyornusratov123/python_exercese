def exception_log(func):
    def wrapper(*args,**kwargs):
        try:
            func()
        except Exception as err:
            print(f"error type: {type(err)}")
    return wrapper

@exception_log
def myfunc():
    print("i am working ...")
    raise PermissionError ("this is permission error")
myfunc()



