#TUPLES

API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])

t = tuple()
print(t)

# Conversion List to Tuple
t1 = tuple(["pramod", "amit", "manisha"])
print(t1)

del t1
# print(t1)

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][0])
print(new_tuple[0][0][0])

q, w, e = (45, 56, 78)
print(q)
print(w)
print(e)

# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("New Delhi" in cities)

# Unpacking of a Tuple
t = (12, 23, 34, 56)
a, b, c, d = (12, 23, 34, 56)

# We CANNOT APPEND new value in the Tuple, in case we want to then
# we have to create a new tuple or convert the tuple into LIST and then APPEND

new_t=t+ (100,)
print(new_t)

my_list=list(t) #CONVERT TUPLE TO LIST
print(my_list)
my_list.append(101)
print(my_list)
t2=tuple(my_list) #CONVERT LIST TO TUPLE
print(t2)