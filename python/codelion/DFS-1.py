#DFSew
#일단 탐색할 수 있을 때까지 탐색하고
#더이상 탐색할 대상이 없으면 갈림길로 돌아와서 다시 탐색
import sys

ans = -1
def dfs(l, y, x, s):
    global ans
    if y == len(l):
        if ans < s:
            ans = s
        return
    print(y, x)
    dfs(l, y + 1, x, s + l[y][x])
    dfs(l, y + 1, x + 1, s + l[y][x])

n = int(sys.stdin.readline())
l = []
for i in range(n):
    ll = list(map(int, sys.stdin.readline().split()))
    l.append(ll)

print(l)
dfs(l, 0, 0, 0)
print(ans)