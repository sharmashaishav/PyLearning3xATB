# Task #2
# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
import math

num = 4
print("The square of number 4 is", num ** 2)  # This will give value of square of 4 i.e. 4x4
print("The cube of number 4 is", pow(num,3))  # This will give value of cube of 4 i.e. 4x4x4



Num1 = float(input("Enter the first number\n"))
Num2 = float(input("Enter the second number\n"))
print("First number is greater or equals to second"if Num1 >= Num2 else"First number is Less than second number")
