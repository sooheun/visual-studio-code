# graph:객체와 관계로 이루어진 자료 구조
# vertex(정점)와 edge(간선)로 이루어진 자료구조
# 명시적 그래프: sns관계, 스타크래프트 빌드 오더, 지하철 노선도
# 암시적 그래프: 바둑, 8-puzzle, 부분수열의 합

"""
        - 3 -
1 - 0           4
        - 2 -
"""

n = 5
d = [[ 0 for i in range(n)] for j in range(n) ]
d[1][0] = d[0][1] = 1
d[0][2] = d[2][0] = 1
d[3][0] = d[0][3] = 1
d[3][4] = d[4][3] = 1
d[2][4] = d[4][2] = 1

for i in range(n):
    print(d[i])