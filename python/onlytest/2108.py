import sys

t = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(t)]
many = []
nums.sort()

aver = sum(nums)/len(nums)

if aver > 0:
    if (aver - int(aver)) >= 0.5 :
        print(int(aver) + 1)
    else:
        print(int(aver))
elif aver < 0:
    if (aver - int(aver)) <= -0.5:
        print(int(aver) - 1)
    else:
        print(int(aver))
else:
    print(0)


print(nums[(t-1)//2])

cnt = 1
if t != 1:
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            if i == len(nums) - 2:
                cnt += 1
                many.append(cnt)
            else:
                cnt += 1
        else:
            many.append(cnt)
            cnt = 1

    # print(nums)
    # print(many)

    if many.count(max(many)) == 1:
        print(nums[sum(many[0:many.index(max(many))])])
    else:
        f_most = many[many.index(max(many))]
        many[many.index(max(many))] = 0
        # print(many)
        # print(f_most)
        print(nums[sum(many[0:many.index(max(many))]) + f_most])

    print(max(nums) - min(nums))
else:
    print(nums[0])
    print(0)
