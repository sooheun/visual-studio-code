count = int(input("")) # 테스트 케이스
location = []
star = 0
answer = []
check = 0

for i in range(0, count): #출발점 도착점
    star_r = []
    
    location.append([int(num) for num in input().split(" ", 3)])
    
    star = int(input("")) # 행성계 개수
    
    for a in range(0,star): #행성계 좌표, 반지름
        star_r.append([int(num) for num in input().split(" ", 2)])
    
    check = 0
    
    for a in range(0, len(star_r)):
        s_R = (location[i][0]-star_r[a][0])**2 + (location[i][1]-star_r[a][1])**2
        f_R = (location[i][2]-star_r[a][0])**2 + (location[i][3]-star_r[a][1])**2

        if s_R < (star_r[a][2])**2 or f_R < (star_r[a][2])**2:
            
            if s_R < (star_r[a][2])**2 and f_R < (star_r[a][2])**2:
                pass
            else:
                check += 1
   
    answer.append(check)

for i in answer:
    print(i)