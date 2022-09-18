#dynamic_programming: 복잡한 문제를 간단한 문제로 나누어 해결

import sys

"""
1. dp식 정의: d[i] = i숫자로 만드는데 드는 최소 연산 수
2. dp식 세우기: d[i] = min(d[i*3], d[i*2], d[i + 1]) + 1
3. dp식 초기화: d[all] = inf, d[n] = 0
"""

n = int(sys.stdin.readline())
inf = 99999999
d = [ inf for i in range(3*n + 1)]
d[n] = 0

for i in range(n - 1, 0, -1):
    d[i] = min(d[i * 3], d[i * 2], d[i + 1]) + 1
for i in range(1, n + 1):
    print(i, d[i])