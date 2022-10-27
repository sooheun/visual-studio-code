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


def binary_search(array, find, start, end):
    while start <= end:    
        mid = (start + end) // 2
        if array[mid] == find:
            return True
        if array[mid] < find:
            start = mid + 1
        else:
            end = mid - 1

    return False


t = int(input(""))

nums = list(map(int, input("").split()))

n = int(input(""))

finds = list(map(int, input("").split()))

nums = merge_sort(nums)

for i in finds:
    if binary_search(nums, i, 0 , t - 1):
        print(1)
    else:
        print(0)