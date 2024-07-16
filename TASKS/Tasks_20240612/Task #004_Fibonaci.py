def fib():

 a, b = 0, 1
 c = 0
 n = int(input("Enter a number till which you want to view Fibonaci series\n"))
 if n <= 0:
    print("Enter a valid positive integer:\n")

 else:
    for i in range(0, n + 1):
        print(c)
        a = b
        b = c
        c = a + b
fib()