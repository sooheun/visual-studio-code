count = int(input(""))

numbers = []
distance = 0

for i in range(0,count):

    numbers.append([int(num) for num in input().split(" ", 5)])

x1 = 0
y1 = 0
x2 = 0
y2 = 0

plus_r = 0
sub_r = 0

answer = 0

for i in range(0,count):
    x1 = numbers[i][0]
    y1 = numbers[i][1]
    x2 = numbers[i][3]
    y2 = numbers[i][4]

    if numbers[i][2] < numbers[i][5]:
        plus_r = numbers[i][5] + numbers[i][2]
        sub_r = numbers[i][5] - numbers[i][2]
    else:
        plus_r = numbers[i][5] + numbers[i][2]
        sub_r = numbers[i][2] - numbers[i][5]  
    
    distance = (x1-x2)**2 + (y1 - y2)**2
    
    print(plus_r,sub_r,distance)

    if sub_r**2 < distance and distance < plus_r**2:
        answer = 2
    elif sub_r == 0 and x1 == x2 and y1 == y2:
        answer = -1
    elif plus_r**2 == distance or sub_r**2 == distance:
        answer = 1
    elif plus_r**2 < distance or distance < sub_r**2 or distance == 0:
        answer = 0
    print(answer)