# Implement a call-logger decorator with history tracking

#     Keep a list (closure-based) that stores each function call’s arguments and return value.
#     Provide an inner function get_history() accessible from the wrapped function (e.g., func.history()) to inspect call history.

def his(func):
    history=[]
    def wrapper(*args,**kwargs):
        nonlocal history
        try:
            res=func(*args,**kwargs)
        except Exception as e:
            res=e
            history.append(
                
                {
                    "args": args,
                    "kwargs": kwargs,
                    "res":res
                }
                
            )
            return res
        


    def get_history():
        nonlocal history
        return history 
        
    wrapper.history=get_history
    return wrapper

@his 
def add(a,b):
    return a+b
print(add(2,3))
print(add(78,98))
@his 
def div(a,b):
    return a/b
print(div(2,4))
print(div(2,0))
print(add.history())
