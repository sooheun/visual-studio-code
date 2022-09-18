#백준 1699
"""
정의d[i] = i수를 제곱수로 표현할 대에 그 항의 최소개수

식 세우기
d[i] = min(d[i], d[i-j*j] + 1)

식 초기화
d[i] = i
"""

import sys
n = int(sys.stdin.readline())
d = [i for i in range(n + 1)]
for i in range(2, n + 1):
    for j in range(2, i + 1):
        if i < j*j:
            continue
        d[i] = min(d[i], d[i-j*j] + 1)
print(d[n])