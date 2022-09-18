import sys

t = int(sys.stdin.readline())

xy = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

xy.sort()
# print(xy)

# for i in range(len(xy)):
#     for j in range(len(xy)-1):
#         if xy[j][0] > xy[j+1][0] or (xy[j][0] == xy[j+1][0] and xy[j][1] > xy[j+1][1]):
#             temp = xy[j]
#             xy[j] = xy[j+1]
#             xy[j + 1] = temp

for i in xy:
    for j in range(len(i)):
        print(i[j], end=" ")
    print("")