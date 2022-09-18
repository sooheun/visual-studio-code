num = int(input(""))

cand = 0
result = []

for i in range(1, num):
    cand = 0
    cand += i
    for j in str(i):
        cand += int(j)
    if(cand == num):
        result.append(i)

if len(result) == 0:
    print(0)
else:
    print(min(result))