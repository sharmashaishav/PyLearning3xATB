# ✅ 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

Side1 = float(input("Enter the length of first side\n"))
Side2 = float(input("Enter the length of second side\n"))
Side3 = float(input("Enter the length of third side\n"))

if Side1 == Side2 == Side3:
    print("This is an Equilateral Triangle with all the sides of same length")
elif (Side1 != Side2) and (Side1 != Side3) and (Side3 != Side2):
    print("This is an Scalene triangle with NO sides of same length")
else:
    print("This is an Isosceles Triangle with only two sides of same length")
