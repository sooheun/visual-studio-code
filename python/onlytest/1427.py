import sys

num = sys.stdin.readline()

result = []
for i in num:
    result.append(i)

result.sort()
result.reverse()

for i in result:
    print(i, end="")

