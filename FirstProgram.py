def decorator_func(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator_func
def greet():
    print("Hello")

greet()
