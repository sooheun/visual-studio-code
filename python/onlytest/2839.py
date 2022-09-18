num = int(input(""))

cnt = 0
no = 0

while num > 0:
    if num % 5 == 0:
        cnt = cnt + (num / 5)
        num = num % 5
        
    elif num % 3 == 0:
        num -= 3
        cnt += 1
        
    elif num > 5:
        num -= 5
        cnt += 1
    else:
        print(-1)
        no = 1
        break

if no == 0:
    print(int(cnt))