from multiprocessing.connection import answer_challenge
import sys
import random


n, m = map(int, sys.stdin.readline().split())
paper = list(map(int, sys.stdin.readline().split()))
paper.sort()

def bs(l, v):
    le = 0
    ri = len(l)- 1
    while le <= ri:
        mid = (le + ri) // 2
        if l[mid] == v:
            return True
        elif l[mid] < v:
            le = mid + 1
        else:
            ri = mid - 1
    return False

n2l = []
for i in range(n):
    for j in range(n):
        n2l.append(paper[i] + paper[j])  
n2l.sort()

ans = 0
for i in range(len(n2l)):
    if bs(n2l, m - n2l[i]):
        ans = 1



# ans = 0
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             s = paper[i]+ paper[j] + paper[k]

#             if bs(paper, m - s):
#                 ans = 1

print(ans)