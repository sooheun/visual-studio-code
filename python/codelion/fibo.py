import sys

def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 2)

n = int(sys.stdin.readline())
print(f(n))