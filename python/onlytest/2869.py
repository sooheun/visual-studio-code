nums = list(map(int, input("").split()))

if((nums[2] - nums[0])%(nums[0] - nums[1]))==0:
    print((nums[2] - nums[0])//(nums[0] - nums[1])+1)
else:
    print(((nums[2] - nums[0])//(nums[0] - nums[1]))+2)
