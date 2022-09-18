count = int(input(""))

number = list(map(int, input("").split()))

average = ((sum(number)/max(number))*100)/count
print(average)