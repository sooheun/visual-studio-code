import math

start_deg = 0
end_deg = 360
width = 120

values = []
def roundUp(num): # 반올림 함수
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        int(num)

def print_hyphen(count): # 위에 x, sinx 표시
    for i in range(count):
        print('-', end='')

def print_space(count): # 공백 출력
    for i in range(count):
        print(' ', end='')

def print_graph(width, start_deg): # 그래프를 한줄 씩 출력 (120, 0)
    print("%0.3d" % start_deg, end='')
    left_half = round((width-1) / 2)
    right_half = width - left_half
    value = round(math.sin(math.radians(start_deg)), 3)
    values.append(value)
    loc = round(((value+1)*(width//2)))
    
    if value > 0:
        print_space(left_half)
        print('|', end='')
        print_space(loc-1-left_half-1)
        print('*', end='')
        print_space(width-loc+2)
    
    elif start_deg == 0 or start_deg % 180 == 0:
        print_space(left_half)
        print('*', end='')
        print_space(right_half + 1)
        
    else:
        print_space(loc)
        print('*', end='')
        print_space(left_half-loc-1)
        print('|', end='')
        print_space(right_half)
    
    print("%.3f" % value)

def print_sin(start_deg, end_deg, width, length): # 0 ~ 350 까지 반복
    for i in range(length):
        if start_deg  == end_deg:
            break
        else:
            print_graph(width, start_deg)
            start_deg += 10

def main():
    print(' x', end=' ')
    print_hyphen(width)
    print(' sin(x)')
    
    
print(' x', end=' ')
print_hyphen(width)
print(' sin(x)')
print_sin(start_deg, end_deg, width, 57)

for i in range(len(values)):
    print(i, values[i])