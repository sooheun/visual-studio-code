def gcd(a, b): #최대 공약수 구하기
    for i in range(2, min(a, b)):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

def gcd2(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b

def gcd3(a, b): # 2번 함수 재귀 함수 버전
    if b:
        return gcd(b, a % b)
    return a

def gcd4(a, b):
    return gcd4(b, a % b) if b else a #3번 함수 한줄 버전

import sys

t = int(sys.stdin.readline())
for tc in range(t):
    l = list(map(int, sys.stdin.readline().split()))
    n = l[0]
    l = l[1:]
    ans = 0
    for i in range(len(l)-1):
        for j in range(i + 1, len(l)):
            ans += gcd4(l[i], l[j])
    print(ans)