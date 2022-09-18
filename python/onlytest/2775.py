count = int(input(""))

result = []

for i in range(0, count):
    factorial = 1
    bunza = 1
    
    floor = int(input(""))
    house_n = int(input(""))

    for j in range(1, floor+2):
        factorial *= j

    for k in range(house_n, house_n + floor + 1):
        bunza *= k
    
    result.append(bunza/factorial)

for a in result:
    print(int(a))
