# Recursion - it is programming technique where function calls itself in order to perform a task
#
# 1. Base Case
# 2. Recursive Case

def factorial(n):
    # Base Case
    if n==0 or n==1:
        return 1
    # Recursive Case
    else:
        return n* factorial(n-1)
print(f"Factorial of the number is :\n ",factorial(6))


# Sum of the digits in a number
# Using FOR Loop
def sum_of_digits(n1):
    if n1<10:
        return n1
    else:
        return n1%10 + sum_of_digits(n1//10)
print(f"Sum of the digits of number using FOR loop : \n",sum_of_digits(123456789))

# Using While Loop
def sum_ofdigits(n):
    sum_digit=0
    while n>0:
        sum_digit = sum_digit+n%10
        n=n//10
    return sum_digit
print(f"Sum of the digits of number using WHILE loop : \n",sum_ofdigits(1234567890))