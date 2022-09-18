num = int(input(""))
room = 1
cnt = 1


if num == 1:
    print(1)
else:
    while True:
        room += (cnt * 6)

        if(num <= room):
            print(cnt+1)
            break
        cnt += 1