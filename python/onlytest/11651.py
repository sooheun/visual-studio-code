import sys

t = int(sys.stdin.readline())

xy = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

xy.sort(key=lambda x:(x[1], x[0]))

for i in xy:
    for j in range(len(i)):
        print(i[j], end=" ")
    print("")