count = int(input(""))
num = count

for i in range(0, count):
    word = input("")
    for j in range(0, len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            num = num - 1
            break
print(num)