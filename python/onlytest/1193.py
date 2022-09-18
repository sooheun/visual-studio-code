count = int(input(""))

num = 0
i = 1

while True:
    num += i
    
    if count <= num:
        result = count  - (num - i) 
        break
    i += 1

if (i % 2 == 0):
    print("{}/{}".format(result, i - result + 1))
else:
    print("{}/{}".format(i - result + 1, result))