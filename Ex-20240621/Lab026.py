# Decorators
# What is a Decorator?
# A decorator is essentially a function that takes another function as an argument
# returns a new function that usually extends the behavior

def my_decorator(func):
    def wrapper():
        print(f"Starting the function {func.__name__} ........")
        print("****************************************")
        func()
        print("****************************************")
        print(f"Ending the function {func.__name__}..........")
    return wrapper()


@my_decorator
def hello():
    print("Saying Hello using Decorator")

@my_decorator
def print_():
    print(list(map(lambda num: num / 2, [2, 4, 6, 8, 10])))
