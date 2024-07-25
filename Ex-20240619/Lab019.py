import warnings

global_var = 10
def my_function():
    local_var = 11
    print("Hello")
    print("Local variable:", local_var)

    def inner_function():
        print("inner function calling variable from outer function", local_var)

    inner_function()

print("Global variable:", global_var)
my_function()
