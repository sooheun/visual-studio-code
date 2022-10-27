import sys

n,m = map(int, sys.stdin.readline().rstrip().split())

five = 0
two = 0

for i in range(1, 14):
    if n < 5 ** i:
        break

    if 5 ** i <= n:
        five += n // (5 ** i)
    if 5 ** i <= m:
        five -= m // (5 ** i)
    if 5 ** i <= n-m:
        five -= (n-m) // (5 ** i)

for i in range(1, 31):
    if n < 2 ** i:
        break

    if 2 ** i <= n:
        two += n // (2 ** i)
    if 2 ** i <= m:
        two -= m // (2 ** i)
    if 2 ** i <= n-m:
        two -= (n-m) // (2 ** i)

if five  == 0 or two == 0:
    print(0)
elif five >= two:
    print(two)
else:
    print(five)
