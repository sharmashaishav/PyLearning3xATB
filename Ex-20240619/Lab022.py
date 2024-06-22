# List function - collection of items where duplicate is allowed

my_list = [1,2,3,"Shaishav","Sharma","Vanya","Richa"]

# Indexing
print("Element at index 5: \n",my_list[5])

# Changing an element
my_list[2]=21
print("List after changing the element at index 2:\n",my_list)

# append
my_list.append("Family")
print("List after appending:\n",my_list)

# Extend
my_list.extend(["Sudha Mumma","Jack Papa"])
print("List after extending the items: \n",my_list)

# Insert
my_list.insert(2,7)
print("List after inserting an item at indesx 2:\n",my_list)

# remove
my_list.remove(1)
print("List after removing certain values: \n",my_list)

# Copying a List
my_list_copy=my_list.copy()
print(my_list_copy)

my_list.clear()
print(my_list)
print(my_list_copy)
