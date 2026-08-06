def loggers(func):
    def wrapper():
        print("Decoders function called")
        func()
    return wrapper

@loggers
def dummy():
    print("Hello")

dummy()