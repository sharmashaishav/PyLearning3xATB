# Filters in Python
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def is_even(num):
    return num % 2 == 0


def is_odd(num1):
    return num1 % 2 != 0


even_numbers = list(filter(is_even, num_list))
print(even_numbers)

odd_numbers = list(filter(is_odd, num_list))
print(odd_numbers)
