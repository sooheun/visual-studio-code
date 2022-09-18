count = int(input(""))

num = [list(map(int, input("").split())) for i in range(count)]

sum = 0
average = 0   
stu = 0
answer= []


for i in num:    
    sum = 0
    average = 0
    stu = 0
    for j in range(1,len(i)):
        sum += i[j]
    
    average = sum/i[0]
    
    for k in range(1, len(i)):
        if average < i[k]:
            stu += 1
    
    answer.append((stu/i[0])*100)

for i in answer:
    print("{:.3f}%".format(i))