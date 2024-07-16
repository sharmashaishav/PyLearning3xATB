val = None
#val = val+1 # unsupported operand type(s) for +: 'NoneType' and 'int'
# Data Type  - NoneType
print(val)
# Nothing
# None is not a default value
# None is not 0.
# None is not an empty string.
# None is not the same as False.

name = "" # empty String - memory allocated
print(id(name))
name = None
print(type(name)) # NoneType
print(id(name))
print(name)
name = "Shaishav"
print(name)
print(id(name))

# Escape Seq
print("Hello \"World\"")
print("Hello \nWorld")
print("Hello \tWorld")
print("Hello \bWorld")
