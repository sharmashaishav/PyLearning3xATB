# Task #1
# Explain the difference between the = operator and the == operator in Python.
# What does the ** operator do in Python, and how is it used?
# What does the ^ operator do in Python, and in what context is it commonly used?

name = 'Shaishav'  # '=' Assigns the value/values on the right to the variable name mentioned on the left of '=' operator
name1 = "ShaishavSharma"
print(name)
print(name1)
# Comparison operators are used to compare two values
print("True" if name == name1 else "False")  # Here we are comparing 2 string values
print(
    10 == 2 + 8)  # This will return as true as comparison has a lower precedence than addition, and we need to calculate the addition first.

# ** operator acts as power function pow()
num = 4
print(4 ** 2)  # This will give value of square of 4 i.e. 4x4
print(4 ** 3)  # This will give value of cube of 4 i.e. 4x4x4

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
print(6 ^ 3)

# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 5 = 0000000000000101
# ====================

