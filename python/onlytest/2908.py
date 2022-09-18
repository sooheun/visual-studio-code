from audioop import reverse


nums = list(map(str, input().split()))
r_nums = []

for i in nums:
    r_nums.append(i[::-1])

print(max(r_nums))