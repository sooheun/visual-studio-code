count = int(input(""))

words = [[x for x in input().split()]for y in range(count)]

for i in words:
    cnt = int(i[0])
    for j in i[1]:
        print(j*cnt, end="")
    print("")