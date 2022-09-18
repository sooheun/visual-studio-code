def is_prime(n): # O(N)
    if n <= 1:
        return False
    for i in range(2, n):
        if n  % i == 0:
            return False
    return True

from math import sqrt
def is_prime2(n): # O(sqrt(N))
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def eratosthenes_sieve(n): # 에라토스테네스의 체
    b = [True for i in range(n + 1)]
    b[1] = False
    for i in range(2, int(sqrt(n))+ 1):
        if b[i]:
            for j in range(i*i, n + 1, i):
                b[j] = False
    return b
def is_prime_(b, n):
    return b[n]

b = eratosthenes_sieve(100) #O(N log log N)
print(is_prime_(b, 7))
for i in range(1, 20):
    if is_prime_(b, i): # O(1)
        print(i)