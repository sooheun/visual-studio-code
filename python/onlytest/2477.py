import sys

cham = int(sys.stdin.readline())
dir_dis = []

# 동쪽 : 1 , 서쪽 : 2, 남쪽 : 3, 북쪽 : 4

for i in range(6):
    dir_dis.append(list(map(int, sys.stdin.readline().rstrip().split())))

# print(dir_dis)

max_12 = 0 #동 서 중 최대 값
max_34 = 0 #남 북 중 최대 값

index_12 = 0
index_34 = 0

for i in range(6):
    if dir_dis[i][0] == 1 or dir_dis[i][0] == 2: #동쪽 이나 서쪽
        if dir_dis[i][1] > max_12:
            max_12 = dir_dis[i][1]
            index_12 = i
    else: # 남쪽 이나 북쪽
        if dir_dis[i][1] > max_34:
            max_34 = dir_dis[i][1]
            index_34 = i

# print(index_12, index_34)

big = dir_dis[index_12][1] * dir_dis[index_34][1]

small_one = 0
small_two = 0

if index_12 + 1 > 5:
    if dir_dis[index_12 - 1][1] > dir_dis[0][1]:
        small_one = dir_dis[index_12 - 1][1] - dir_dis[0][1]
    else:
        small_one = dir_dis[0][1] - dir_dis[index_12 - 1][1]
else:
    if dir_dis[index_12 - 1][1] > dir_dis[index_12 + 1][1]:
        small_one = dir_dis[index_12 - 1][1] - dir_dis[index_12 + 1][1]
    else:
        small_one = dir_dis[index_12 + 1][1] - dir_dis[index_12 - 1][1]

if index_34 + 1 > 5:    
    if dir_dis[index_34 - 1][1] > dir_dis[0][1]:
        small_two = dir_dis[index_34 - 1][1] - dir_dis[0][1]
    else:
        small_two = dir_dis[0][1] - dir_dis[index_34 - 1][1]
else:  
    if dir_dis[index_34 - 1][1] > dir_dis[index_34 + 1][1]:
        small_two = dir_dis[index_34 - 1][1] - dir_dis[index_34 + 1][1]
    else:
        small_two = dir_dis[index_34 + 1][1] - dir_dis[index_34 - 1][1]


print((big - small_one * small_two) * cham)

