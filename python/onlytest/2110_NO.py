import sys

def merge_sort(arr): #  병합 정렬
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr



n, c = map(int, sys.stdin.readline().rstrip().split())

nums = merge_sort([int(sys.stdin.readline().rstrip()) for i in range(n)])

if c == 2:
    print(nums(len(nums)-1) - nums[0])
else:
