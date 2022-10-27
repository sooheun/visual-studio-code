import sys

t = int(sys.stdin.readline())

words = [sys.stdin.readline().rstrip() for i in range(t)]

for i in words:
    if i[0].islower():
        i = i[0].upper() + i[1:]
        print(i)
    else:
        print(i)