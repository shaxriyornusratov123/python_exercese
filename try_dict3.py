def decorator(func):
    def wrapper(*args,**kwargs):
        try:
            func()
        except KeyError as e:
            raise ValueError(e)
    return wrapper
@decorator
def myfunc():
    d=dict()
    print(d["key1"])

myfunc()