hh , mm = map(int, input("").split(":"))

area = list(map(int, input("").split()))

l = int(input(""))

event = []
now_area = 0

ss = 0

for i in range(l):
    t , eve = input("").split()
    event.append([float(t), eve])

for i in event:
    ss = i[0]
    if ss >= 60 or sum(area) == 0:
        break
    if mm >= 60:
        hh += 1
        mm -= 60
    if hh >= 12:
        hh -= 12
    now_area = (hh // 2) + 1

    
    if i[1] == "^":
        area[now_area-1] = 0
    elif "MIN" in i[1]:
        mm += int(i[1][0:2])
    else:
        hh += int(i[1][0])


if sum(area) > 100:
    print(100)
else:
    print(sum(area))