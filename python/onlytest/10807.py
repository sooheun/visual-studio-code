t = int(input(""))
nums = list(map(int, input("").split()))
find = int(input(""))
cnt = 0
    
for i in nums:
    if i == find:
        cnt += 1

print(cnt)