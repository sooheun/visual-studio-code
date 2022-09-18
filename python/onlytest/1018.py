row, col = map(int, input("").split())
board = [input("") for _ in range(row)]

result = []
fb = 0
fw = 0

for i in range(0, row-7):
    for j in range(0, col-7):
        fb = 0
        fw = 0
        for k in range(i, i+8): # 행
            for p in range(j, j+8):# 열
               
                if (k + p) % 2 == 0: # 짝수 번
                    if board[k][p] != "W":
                        fw += 1 #칸이 W가 아니므로 W을 새로칠하기 위해 카운트 추가
                    else:
                        fb += 1
                else: # 홀수 번
                    if board[k][p] != "B":
                        fw += 1
                    else:
                        fb += 1
        result.append(fw)
        result.append(fb)
print(min(result))