# ✅ 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

Year = int(input("Enter a year:\n"))
if (Year%4 == 0 and Year%100 !=0) or (Year%100==0 and Year%400==0):
    print(f"{Year} is a Leap Year")
else:
    print(f"{Year} is NOT a Leap Year")

# ✅ #4. Fibonaci series
# # 0,0+1, 0+1+1,
#
# # n = 7
#
# # 0, 1, 2, 3, 5, 8, 13