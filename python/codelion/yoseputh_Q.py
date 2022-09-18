import sys
from queue import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    front = q.popleft()
    return front

n, k = list(map(int, sys.stdin.readline().split()))
queue = deque()
for i in range(1, n + 1):
    queue_push(queue, i)
print(queue)
ans = []
while len(queue) != 0:
    for i in range(k - 1):
        front = queue_pop(queue)
        queue_push(queue, front)
    ans.append(queue_pop(queue))

print(ans)

# 1 2 3 4 5 6 7 (k=3)
# 2 3 4 5 6 7 1: 1번 돌림 (pop => push)
# 3 4 5 6 7 1 2: 2번 돌림
# 4 5 6 7 1 2: 맨 앞을 날림/3
# 5 6 7 1 2 4: 1번
# 6 7 1 2 4 5: 2번
# 7 1 2 4 5: 맨 앞을 날림 /6
# (반복) (n-1번 만큼 회전후 맨앞을 뽑음)