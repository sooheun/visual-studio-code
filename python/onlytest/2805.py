import sys       

k, n = map(int, sys.stdin.readline().rstrip().split())

woods = list(map(int, sys.stdin.readline().rstrip().split()))

start = 1

end = max(woods)

def binary(woods, n, start, end):
    while start <= end:
        answer = 0
        mid = (start + end) // 2

        for i in woods:
            if i - mid > 0:
                answer = answer + (i - mid)
        
        # print(start, mid, end, answer)
        if answer >= n:
            start = mid + 1
        else:
            end = mid - 1
        
    return end

print(binary(woods, n, start, end))