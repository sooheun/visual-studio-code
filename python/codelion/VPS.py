# 괄호의 짝이 맞으면 yes 아니면 no 출력
import sys


def stack_push(stack, value):
    stack.append(value)

def stack_pop(stack):
    last = stack.pop()
    return last

T = int(sys.stdin.readline())
for j in range(T):
    stack = []
    ok = True
    s = sys.stdin.readline().strip() #개행 문자 삭제
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack_push(stack, s[i])
        else:
            if len(stack) == 0:
                ok == False
                break
            last = stack_pop(stack)
            if s[i] == ')':
                if last == '(':
                    continue
                else:
                    ok = False
                    break
            elif s[i] == '}':
                if last == '{':
                    continue
                else:
                    ok = False
                    break
            else:
                if last == '[':
                    continue
                else:
                    ok = False
                    break
    if len(stack) != 0:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")