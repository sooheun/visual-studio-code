n_num = set(i for i in range(1,10001))
un_self_num = set()
sum = 0

for i in range(1,10001):
    sum = i
    for j in str(i):
        sum += int(j) 
    un_self_num.add(sum)

self_num = sorted(n_num - un_self_num)
for i in self_num:
    print(i)
