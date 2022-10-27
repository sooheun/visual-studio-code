def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    divisorsList.remove(1)
    return divisorsList

def gcd(a, b): #a 와 b(a > b)의 최대공약수는 b와 a%b의 최대공약수와 같다.
    na = 0 
    while (b != 0):
        na = a % b
        a = b
        b = na
    
    return a

cnt = int(input(""))

nums = [int(input("")) for i in range(cnt)]

differ = []

if len(set(nums)) == 1:
    for i in getMyDivisor(nums[0]):
        print(i, end=" ")
elif cnt == 2:
    for i in getMyDivisor(abs(nums[0] - nums[1])):
        print(i, end=" ")
else:
    for i in range(len(nums)-1):
        differ.append(abs(nums[i+1] - nums[i]))

    differ = sorted(differ)
    
    gcd_n = differ[0]
    
    for i in range(1, len(differ)):
        gcd_n = gcd(gcd_n, differ[i])

    for i in getMyDivisor(gcd_n):
        print(i, end=" ")