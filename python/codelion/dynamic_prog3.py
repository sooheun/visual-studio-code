#백준 1932

"""
정의 d[i][j] = i,j 위치까지 내려오는데 얻을 수 있는 최대값

식 세우기
d[i][j] = max(d[i-1][j-1], d[i-1][j]) + score[i][j]

식 초기화
d[0][0] = score[0][0]
"""

import sys

n = int(sys.stdin.readline())
l = []
d = []
for i in range(n):
    ll = list(map(int, sys.stdin.readline().split()))
    l.append(ll)
    d.append([0 for j in range(len(ll))])
d[0][0] = l[0][0]
for i in range(1, n):
    for j in range(len(l[i])):
        left = d[i-1][j-1] if j > 0 else 0
        right = d[i-1][j] if j < len(l[i-1]) else 0
        d[i][j] = max(left, right) + l[i][j]
ans = max(d[n-1])
print(ans)