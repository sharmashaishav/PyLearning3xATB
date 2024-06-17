import math

# n = int(input("Enter a number to find its factorial: \n"))
# print(f"Factorial of the given number {n} is :", math.factorial(n))

factorial = 1
n = 5

for i in range(1, n+1):
    factorial = factorial * i
print(factorial)


