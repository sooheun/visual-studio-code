#Queue:먼저 넣는게 먼저 나오는 구조

queue = []

queue.append(5)
queue.append(6)
queue.append(7)

front = queue.pop(0)
print(front)
print(queue)

stack = []
stack.append(5)
stack.append(6)
stack.pop()
# [1, 2, 3, 4, 5] => [-, 2, 3, 4, 5] =>[2, 3, 4, 5]
# deque: 앞에서 넣고 뺄 수 있고, 뒤에서 넣고 뺄 수도 있다.
from queue import deque

dq = deque()
dq.append(5)
dq.append(6)
dq.append(7)
dq.append(8)
front = dq.popleft() # O(1)
print(front)
print()

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    front = q.popleft()
    return front

queue = deque()
queue_push(queue, 5)
queue_push(queue, 6)
queue_push(queue ,7)
front = queue_pop(queue)
print(front, queue)