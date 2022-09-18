# 백준 1260
import sys
from queue import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    front = q.popleft()
    return front

n, m, v = list(map(int, sys.stdin.readline().split()))

d = [ [] for i in range(n + 1) ]
for i in range(m):
    s, e = list(map(int, sys.stdin.readline().split()))
    d[s].append(e)
    d[e].append(s)

for i in range(1, n + 1):
    d[i].sort()

def dfs(d, pos, vis):
    print(pos, end=' ')
    vis[pos] = True
    for i in range(len(d[pos])):
        if vis[d[pos][i]]:
            continue
        dfs(d, d[pos][i], vis)

def bfs(n, d, v):
    vis1 = [ False for i in range(n + 1) ]
    q = deque()
    queue_push(q, v)
    vis1[v] = True
    while len(q) != 0:
        front = queue_pop(q)
        print(front, end=' ')
        for i in range(len(d[front])):
            if vis1[d[front][i]]:
                continue
            vis1[d[front][i]] = True
            queue_push(q, d[front][i])

vis = [ False for i in range(n + 1)]
dfs(d, v, vis)
print()
bfs(n, d, v)