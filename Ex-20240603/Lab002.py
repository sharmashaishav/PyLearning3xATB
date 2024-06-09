# comment in a line by adding hash at start
print("First Day of Python Learning")
print(289031/5)
print(289031.0011)
print(289031.)
print(289031-9281929)
print("Done for the Day")

# Program to find the max in two numbers
print(max(10, 23))
print(max(10, 23, 45))
print(max(10, 23, 45, -1, -2, 100, 1, 87.34))

# TypeError: '>' not supported between instances of 'str' and 'int'
print(max(10, 23, 45, -1, -2, 100, 1))

# ✅ Dynamically typed
# Dynamic Type - Type of Data that Python supports.
age = 65
# variableName = variableValue
# identifier = literal

# Types which are supported in the Python

# Integers - Positive and negative whole numbers.
# 1, -1,123, 999, 100000, 96543210

# Floating Points Numbers
# 3.14, 5.3333333 , 18.00, 0.000786  . -0.4, -1.6
pi = 3.14

# String
# "pramod", "A", "hello world", "Hi, I am good person, You are a liar", "12345"
name = "Pramod"

# Boolean
# True, False
# true, false ? boolean?
isMale = True

# How do I check the type of the variable?
print(type(age))
print(type(name))
print(type(isMale))
print(type(pi))

# Python - Complex NUMBER - i iota -
complex_number = 2 + 3j
# Real - 2
# Imaginary - 3
print(complex_number.real)
print(complex_number.imag)

# Complex Data types in Python
# List
# Tuple
# Dictionary
# Set

age = 65
# Dynamically typed
print(type(age))
age = "sixty five"
print(type(age))