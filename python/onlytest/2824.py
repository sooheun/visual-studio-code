from math import gcd

c_f = int(input(""))
resultf = 1

nums = list(map(int, input("").split()))

for i in nums:
    resultf *= i

c_s = int(input(""))

nums = list(map(int, input("").split()))
results = 1

for i in nums:
    results *= i

result = str(gcd(resultf, results))

print(result[-9:])