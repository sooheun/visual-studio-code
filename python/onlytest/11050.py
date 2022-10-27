import sys

a = 1
b = 1

n,m = map(int, sys.stdin.readline().rstrip().split())

for i in range(n,n-m,-1):
    a *= i

for i in range(2, m+1):
    b *= i


print(int(a/b))