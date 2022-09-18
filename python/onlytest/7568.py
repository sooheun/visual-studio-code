t = int(input(""))
cand = [list(map(int, input().split())) for _ in range(t)]

result = []
for i in range(0, t):
    point = 0
    for k in range(0, t):
        if(i == k):
            continue
        elif(cand[i][0] < cand[k][0] and cand[i][1] < cand[k][1]):
            point += 1
    print(point+1, end=" ")

