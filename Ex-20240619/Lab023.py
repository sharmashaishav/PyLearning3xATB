# Perform a action on a list(action could be to double it or to square the items in it)
my_list = [1, 2, 3, 4, 5]

# using FOR LOOP
temp_list = []
for i in my_list:
    # temp_list.append(i*2) This will print double of the list items
    temp_list.append(i ** 2)
print(temp_list)


# Using Lambda and Map function

# Map()
# 1. Takes Each item from the list
# 2. execute the function on it which we will create.
# 3. Return same number of elements as a list

def my_function(num):
    return num * 2


double_list = list(map(my_function, my_list))
print(double_list)

# In case we dont want to define a function

my_function = lambda num: num + 2
double_list = list(map(my_function, my_list))
print(double_list)

# We can directly define my_function in the map function
double_list = list(map(lambda num: num - 2, my_list))
print(double_list)

# We can further reduce it to single line code

print(list(map(lambda num: num / 2, my_list)))

# instead of fetching the list from my list we can directly give list values
print(list(map(lambda num: num / 2, [2, 4, 6, 8, 10])))
