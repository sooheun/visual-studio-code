n = int(input(""))
five = 5

result = 0

while five <= n:
    result += n // five
    five = five * 5

print(result)