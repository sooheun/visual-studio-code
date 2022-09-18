call = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word = input()
time = 0

for i in range(len(call)):
    for j in word:
        if j in call[i]:
            time += i + 3

print(time)