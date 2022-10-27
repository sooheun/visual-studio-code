def gcd(a, b):
    na = 0 
    while (b != 0):
        na = a % b
        a = b
        b = na
    
    return a

cnt = int(input(""))

lings = list(map(int, input("").split()))

for i in range(1, len(lings)):
    gcd_n = gcd(lings[0], lings[i])
    print(str(lings[0]//gcd_n) + "/" + str(lings[i]//gcd_n))