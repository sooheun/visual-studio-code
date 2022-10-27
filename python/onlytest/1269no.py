import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(a.difference(b)) + len(b.difference(a)))