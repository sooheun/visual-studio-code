#음수를 포함한 수열이 있다. 각 요소를 정하여 총합을 구할 때의 그 값
#입력값 S와 같은 경우의 수의 개수를 구하라
import sys

ans = 0
def dfs(l, s, pos, _sum):
    global ans
    if pos == len(l):
        if _sum == s:
            ans += 1
        return
    dfs(l, s, pos + 1, _sum + l[pos])
    dfs(l, s, pos + 1, _sum)

n, s = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

dfs(l, s, 0, 0)
if s == 0:
    ans -= 1
print(ans)