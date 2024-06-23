from collections import OrderedDict

# Dictionary
# A dictionary is an unordered collection of data
# in a key-value pair format.

my_dict1 = {
    "fname": "Vanya",
    "lname": "Sharma",
    "age": '32',
    "address": "Pune"
}

print(len(my_dict1))
print(my_dict1["fname"])
my_dict1["fname"] = "Shaishav"
print(my_dict1)
print(my_dict1["age"])
print(my_dict1["address"])

phone_book = dict(name="Amit", age=57, address="Delhi")
print(phone_book)

pramod_details2 = \
    {"name": "Shaishav",
     "90": 34.34,
     "isMale": True,
     "Address": "MH"
     }

print(pramod_details2.get("Address"))
print(pramod_details2["Address"])
print(pramod_details2.values())
print(pramod_details2.keys())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95, 'd': 95}
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for k, v in my_dict1.items():
    print(k, v)