count = int(input(""))

num = []
answer = 0

for i in range(1, count+1):
    num = list(map(int, str(i)))

    if i < 100:
        answer += 1
    elif num[2]-num[1] == num[1]-num[0]:
        answer += 1
        


print(answer)