import sys

n, x = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

ans = []

for i in range(n):
    if l[i] < x:
        print(l[i], end=" ")