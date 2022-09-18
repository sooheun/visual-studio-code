import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
pq = PriorityQueue()

for i in range(n):
    a = int(sys.stdin.readline())
    pq.put(a)



ans = 0
while pq.qsize() > 1: #O(Nlog N)
    mn1 = pq.get()
    mn2 = pq.get()
    nxt = mn1 + mn2
    ans += nxt
    pq.put(nxt)

print(ans)