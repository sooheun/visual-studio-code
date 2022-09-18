import sys

n, k = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))


found = False
le = 0
ri= len(l)-1
while le <= ri:
    mid = (le + ri) // 2
    if l[mid] == k:
        found = True
        break
    elif l[mid] < k:
        le = mid + 1
    elif l[mid] > k:
        ri = mid - 1

if found:
    print(1)
else:
    print(0)
