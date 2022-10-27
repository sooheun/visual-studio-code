cnt = int(input(""))

for i in range(cnt):
    variations = {}
    getsu = int(input(""))

    for j in range(getsu):
        name, vari = map(str, input("").split())
        if vari in variations:
            variations[vari] += 1
        else:
            variations[vari] = 1
    nums = list(variations.values())
    result = 1
    for i in nums:
        result = result * (i + 1)
    print(result-1)