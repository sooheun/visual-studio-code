nums = list(map(int, input("").split()))

i = 1

if nums[1] >= nums[2]:
    print(-1)
else:
    print(nums[0]//(nums[2]-nums[1])+1)