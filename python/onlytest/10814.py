import sys

input = sys.stdin.readline
n = int(input())

words = []

for i in range(n):
    a , b = input().split()
    c = [int(a), b]
    words.append(c)

words.sort(key=lambda x: x[0])

for i in words:
    print(i[0], i[1])