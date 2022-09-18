total = int(input(""))
sum = 0

for i in range(int(input(""))):
    money, cnt = map(int, input("").split())
    sum += money * cnt
if(sum == total):
    print("Yes")
else:
    print("No")