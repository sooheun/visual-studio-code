n = int(input())

nums = [0] * 31

nums[2] = 3

for i in range(4, n+2, 2):
    nums[i] = 3 * nums[i-2] + 2
    for j in range(4, i+1, 2):
        nums[i] += 2 * nums[i - j]
        
print(nums[n])