asc = [1,2,3,4,5,6,7,8]

t = list(map(int, input("").split()))

if asc == t:
    print("ascending")
elif list(reversed(asc)) == t:
    print("descending")
else:
    print("mixed")