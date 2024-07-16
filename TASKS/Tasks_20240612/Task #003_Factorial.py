import math

# n = int(input("Enter a number to find its factorial: \n"))
# print(f"Factorial of the given number {n} is :", math.factorial(n))

factorial = 1
n = int(input("Enter the number of which you want factorial\n"))

for i in range(1, n+1):
    factorial = factorial * i
print(factorial)


