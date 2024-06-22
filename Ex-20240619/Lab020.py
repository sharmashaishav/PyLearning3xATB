num = [1, 2, 3]


def do_something(mylist):
    mylist.append("Shaishav")
    mylist[-4] = 4
    return mylist


num.append("Sharma")
L = do_something(num)
print(L)
