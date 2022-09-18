#백준 2606

import sys
from queue import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    front = q.popleft()
    return front

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
d = [[] for i in range(n + 1)]
for i in range(m):
    s, e = list(map(int, sys.stdin.readline().split()))
    d[s].append(e)
    d[e].append(s)

ans = 0
vis = [False for i in range(n + 1)]
q = deque()
queue_push(q, 1)
vis[1] = True
while len(q) != 0:
    ans += 1
    front = queue_pop(q)
    for i in range(len(d[front])):
        if vis[d[front][i]]:
            continue
        vis[d[front][i]] = True
        queue_push(q, d[front][i])
print(ans - 1)

for i in range(1, n + 1):
    print(i, d[i])
