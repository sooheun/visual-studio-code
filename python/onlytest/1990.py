first, last = map(int, input().split())

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  
    return True

if last >= 10000000:
    last = 10000000

for i in range(first, last+1):
    if str(i) == str(i)[::-1] and isPrime(i):
         print(i)
print(-1)


# palin = [i for i in range(first, last+1) if str(i) == str(i)[::-1]]

# for i in palin:
#     if isPrime(i):
#         print(i)
