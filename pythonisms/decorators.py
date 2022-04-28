import functools
from time import time
from functools import wraps

###Timing
def timing(func):
    @wraps(func)
    def time_func(*args,**kwargs):
        time1 = time()
        final = func(*args, **kwargs)
        time2 = time()
        print(f'total time spent: {time2-time1}')
        return final
    return time_func

@timing    
def print_time(ll):
    for i in ll:
        print(i)

ll = ['Hi','my','name','is','chris']
print_time(ll)

### Slow Down

# def slow(func):
#     @functools.wraps(func)
#     def wrap_slow(*args, **kwargs):
#         time.sleep(2)
#         final = func(*args, **kwargs)
#         return final
#     return wrap_slow

# @slow
# def print_time2(str):
#     for i in ll:
#         print(i)

# str = ['Hi','my','name','is','chris']
# print_time2(ll)

### Debug

def Error(func):
    def Function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__}: wrong data type")
    return Function

@Error
def divide(int,l):
    print(int/l)

divide('Hi','hi')

