import sys

t, k = map(int, sys.stdin.readline().split())

items = []
result = []
dp = [[0] * (k+1) for _ in range(t+1)]

for i in range(t):
    kg, value = map(int, sys.stdin.readline().split())
    items.append([kg, value])

for i in range(1, t+1):
    for k in range(1, k+1):
        if items[i-1][0] > k:
            dp[i][k] = dp[i-1][k]
        else:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-items[i-1][0]]+items[i-1][1])

print(dp[t][k])
