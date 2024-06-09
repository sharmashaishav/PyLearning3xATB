# Take the 2 int number from the user and we want to add them.
# We need to use the input() function.

num1 = input("Enter the first value: ")
num2 = input("Enter the second value: ")
# type conversion - str -> int -> ? int()
result = str(num1)+str(num2)
print(result)

#  + ->  int  sum operation
#  + -> str - concat
# int to str -> str()
# str to int -> int()

print(type(result))