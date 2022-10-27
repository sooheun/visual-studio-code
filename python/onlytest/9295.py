cnt = int(input(""))

sums = []

for i in range(cnt):
    sums.append(sum(list(map(int, input("").split()))))

for i in range(cnt):
    print("Case {}: {}".format(i+1, sums[i]))