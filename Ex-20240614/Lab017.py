for y in range(1,10):
    if y%3==0:
              print(y)
    else:
        pass#print(y*2)

# Match Case
# numbers = int(input("Enter a Number\n"))
browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("FF code executed!")
    case _:
        print("No browser Found!")