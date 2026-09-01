import time
from functools import wraps
def loggers(func):
    def wrapper(*arg,**kwargs):
        print("Decoders function called")
        print(*arg,**kwargs)
        return func(*arg,**kwargs)
    return wrapper

@loggers
def dummy(name):
    print(f"Hello {name}")

dummy("Tamil")

def calculate_time(func):
    @wraps(func)
    def wrapper(*arg,**kwargs):
        print("Calculating time")
        start = time.time()
        result = func(*arg,**kwargs)
        end = time.time()
        print(f"Time taken: {end-start}")
        return result
    return wrapper

@calculate_time
def dummy(name):
    time.sleep(2)
    print(f"Hello {name}")

dummy("Tamil")
