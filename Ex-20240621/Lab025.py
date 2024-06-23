#Sets

# Collection of UNIQUE Items (Unordered)
list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
print(list_of_unique_items)


list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1) #Converting the list to set
print(set1)
print(len(set1))

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(len(set1))

for i in set1:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12])
print(len(set1))
set1.remove(5)
print((set1))
print(len(set1))

set1.add(100)
set1.pop()
print((set1))