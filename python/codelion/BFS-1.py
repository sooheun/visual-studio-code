#BFS(너비 우선 탐색)
#갈림길마다 나를 복제해서 갈 수 있는 곳을 동시에 탐색
import sys
from queue import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

n = int(sys.stdin.readline())
l = []
for i in range(n):
    ll = list(map(int, sys.stdin.readline().split()))
    l.append(ll)

q = deque()
ans = -1
queue_push(q, [0, 0, 0])
while len(q) != 0:
    front= queue_pop(q)
    if front[0] == n and ans < front[2]:
        ans = front[2]
    print(front)
    if front[0] < n:
        left = [front[0] + 1, front[1], front[2] + l[front[0]][front[1]]]
        right = [front[0] + 1, front[1] + 1, front[2] + l[front[0]][front[1]]]
        queue_push(q, left)
        queue_push(q, right)

print(ans)