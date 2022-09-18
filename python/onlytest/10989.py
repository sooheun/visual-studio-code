import sys

t = int(sys.stdin.readline())

counting = [0] * 10001

for i in range(t):
    counting[int(sys.stdin.readline())] += 1

num = 0
for i in counting:
    if i != 0:
        for j in range(0, i):
            sys.stdout.write("{}\n".format(num))
    num += 1