# 백준 2579

"""
정의 d[i] = i위치 까지 오면서 얻은 최대 점수

식 세우기
d[i] = max(d[i-2], d[i-3] + score[i-1]) + score[i]

식 초기화
d[0] = score[0], d[1] = score[0] + score[1]
d[2] = score[2] + max(score[0], score[1])
"""

import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
d = [ 0 for i in range(n) ]
d[0] = l[0]
d[1] = l[0] +l[1]
d[2] = l[2] + max(l[0], l[1])

for i in range(3, n): #O(N)
    d[i] = max(d[i-2], d[i-3] + l[i-1]) + l[i]
print(d[n-1])