def gcd(a, b): #a 와 b(a > b)의 최대공약수는 b와 a%b의 최대공약수와 같다.
    na = 0 
    while (b != 0):
        na = a % b
        a = b
        b = na
    
    return a
    
yak = 0

cnt = int(input(""))

for i in range(cnt):
    a, b = map(int, input().split())

    if a > b:
        yak = gcd(a, b)
    else:
        yak = gcd(b, a)
    
    print(a*b//yak) #최소 공배수는 두 수의 곱에 최대 공약수를 나눈 것과 같다