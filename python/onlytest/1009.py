t = int(input(""))

results = []

for i in range(0, t):
    a, b = map(int, input("").split())
    first = []
    
    if str(a)[-1] == '0':
        results.append('10')
        continue

    for j in range(0, 4):
        if str(a ** (j+1))[-1] in first:
            break
        else:
            first.append(str(a ** (j+1))[-1])

    if b % len(first) == 0:
        results.append(first[-1])
    else:
        results.append(first[b % len(first) -1])
for i in results:
    print(i)