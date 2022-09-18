#stack:무더기, 쌓이다, 포개지다
#먼저 넣은게 나중에 나오는 자료 구조
#stack: push(): 차곡차곡 뒤에 추가하는 것
#stack: pop(): 맨 뒤에 있는 원소가 빠져나가는 것

# python: primitive type: int, float, str
# non-primitive type: list, dictionary, set
# primitive type: copy - call by value 함수가 끝나면 효과가 사라짐
# non-primitive type: reference - call by reference 함수가 끝난 이후의 효과가 반영됨
def stack_push(stack, value):
    stack.append(value)

def stack_pop(stack):
    last = stack.pop()
    return last

stack = []
stack_push(stack, 5)
stack_push(stack, 6)
stack_push(stack, 7)
print(stack)
last = stack_pop(stack)
print(stack, last)


# l = []
# l.append(5)
# l.append(6)
# l.append(7)

# print(l)

# a = l.pop()
# print(a)
# print(l)
