count = int(input(""))
question = []
score = 0
plus = 1
scores = []


for i in range(0,count):
    question.append(input(""))
    

    for j in range(0, len(question[i])):
        if "O" == question[i][j]:
            score += plus
            plus += 1
        else:
            plus = 1
    
    scores.append(score)
    plus = 1
    score = 0

for i in scores:
    print(i)
