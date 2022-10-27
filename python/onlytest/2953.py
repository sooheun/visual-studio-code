total_nums = []

for i in range(5):
    total_nums.append(sum(list(map(int, input("").split()))))


print(total_nums.index(max(total_nums)) + 1, max(total_nums)) 