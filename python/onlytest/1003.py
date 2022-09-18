def fibonacci(n):
    a, b = 1, 1
    if (n == 0):
        return 0  
    elif (n == 1):
        return 1
    else:
        for i in range(1, n):
            a, b = b, a + b
        return a

count = int(input(""))

for i in range(count):
    a = int(input(""))
    
    if a == 0:
        print(1, 0)
    else:
        print(fibonacci(a-1), fibonacci(a))