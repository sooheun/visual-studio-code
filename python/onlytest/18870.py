def merge_sort(arr):
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

cnt = int(input(""))

nums = list(map(int, input("").split()))
sorted_nums = merge_sort(list(set(nums)))

dict_nums = {}

for i in range(len(sorted_nums)):
    dict_nums[sorted_nums[i]] = i

for i in nums:
    print(dict_nums[i], end=" ")