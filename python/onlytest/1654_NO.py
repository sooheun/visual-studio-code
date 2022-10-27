import sys

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i = i+1
        else:
            sorted_list.append(right[j])
            j = j+1
    while i < len(left):
        sorted_list.append(left[i])
        i = i+1
    while j < len(right):
        sorted_list.append(right[j])
        j = j+1
    return sorted_list
    
def merge_sort(unsorted_list):
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    else:
        mid = n // 2 
        left = merge_sort(unsorted_list[:mid])
        right = merge_sort(unsorted_list[mid:])
        return merge(left, right)

k, n = map(int, sys.stdin.readline().rstrip().split())

nums = []

for i in range(k):
    nums.append(int(sys.stdin.readline().rstrip()))

nums = merge_sort(nums)

start = 1
end = nums[len(nums)- 1]

mid = 0

correct = []
while start <= end:
    answer = 0
    mid = (start + end) // 2

    for i in nums:
        answer = answer + (i // mid)
    # print(mid)

    if answer >= n:
        correct.append(mid)
        start = mid + 1
    else: # answer < n
        end = mid - 1

print(max(correct))