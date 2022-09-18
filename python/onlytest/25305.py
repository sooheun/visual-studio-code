import sys

count, rank = map(int, input("").split())
scores = list(map(int, input("").split()))

for i in range(len(scores)):
    for j in range(len(scores) - i - 1):
        if(scores[j] < scores[j+1]):
            temp = scores[j]
            scores[j] = scores[j + 1]
            scores[j + 1] = temp

print(scores[rank-1])
