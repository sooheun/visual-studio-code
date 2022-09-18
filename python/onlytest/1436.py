t = int(input(""))

num = 666
check = 1

while True:
    if check == t:
        break
    num += 1
    
    if "666" in str(num):
        check += 1

print(num)