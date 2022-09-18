import sys
from queue import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

n, m = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(n):
    s = sys.stdin.readline().strip()
    l.append(s)

q = deque()
queue_push(q, [0, 0])
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
d = [[ 0 for i in range(m)] for j in range(n)]
d[0][0] = 1
while len(q) != 0:
    front = queue_pop(q)
    for i in range(4):
        ny = front[0] + dy[i]
        nx = front[1] + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if l[ny][nx] != '1':
            continue
        if d[ny][nx] != 0:
            continue
        d[ny][nx] = d[front[0]][front[1]] + 1
        queue_push(q, [ny, nx])

print(d[n-1][m-1])

