import sys

n = int(sys.stdin.readline())

def atobsum(n):
    return (n-1)*(n)//2

nums = sys.stdin.read()

def hap(nums, n):
    a = '' # nums안의 값은 숫자모양의 문자임
    result = 0
    for i in nums:
        if i.isdigit():
            a += i
        elif i == ' ': #공백을 만나면 공백과 공백 사이의 숫자모양의 문자가 c안에 저장되있으므로 c를 더함
            result += int(a)
            a = '' #a 초기화
    result += int(a) #마지막 숫자는 for문 안에서 더해지지 안으므로 마저 더함

    return result - atobsum(n)

print(hap(nums, n))