def greet():
    print("Hello, How are you?")


greet()


def greet1(name="Sharma"):
    print("Hello, How are you?", name)


greet1('Shaishav')
greet1()
greet1(name="Vanya")


def sum(a, b, c):
    return a + b + c
print('END of function definition')

result = sum(31, 4, 9)
print(result)
print(sum(31, 4, 9))
print('Calling the Function')

def print_(*args):
    for i in args:
        print(i,end="\n")

print_('Shaishav','Sharma','Vanya','Sharma\n')
print_('Shaishav','Sharma','Vanya','Sharma',"Richa",'Sharma')

