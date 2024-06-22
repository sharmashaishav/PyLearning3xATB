# Lambda Expression - to perform a code in one line
# salary=2000
def double_my_salary(salary):
    return salary * 2


new_salary = double_my_salary(2000)
print(new_salary)

double_my_salary_with_Lambda = lambda salary: salary * 2
print("Doubled the salary with Lambda", double_my_salary_with_Lambda(2000))

# Find and return Even or Odd number using Lamda expression

check_even_odd = lambda num: "EVEN NUMBER" if num % 2 == 0 else "ODD NUMBER"
print(check_even_odd(int(input("Enter a number to check if it's odd or even number:\n"))))

# square of any number
pow_function = lambda: int(input("Enter a number whose square you want: \n ")) ** 2
print(pow_function())
