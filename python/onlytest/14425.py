import sys

n1, n2 = map(int, sys.stdin.readline().split())

list_s = [(sys.stdin.readline().strip()) for _ in range(n1)] # 5
check_s = [(sys.stdin.readline().strip()) for _ in range(n2)] # 11

list_s.sort()
result = 0

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for i in check_s:
    if(binary_search(list_s, i, 0, len(list_s)-1)):
        result += 1

print(result)
