attack, de = map(int, input().split())

result = attack - attack*(de/100)

if result >= 100:
    print(0)
else:
    print(1)