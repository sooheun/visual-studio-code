import sys

cnt , q = map(int, sys.stdin.readline().split(" "))
pokemon = {}
pokemon_list = []
for i in range(cnt):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = i+1
    pokemon_list.append(name)

result = []
for i in range(q):
    question = sys.stdin.readline().rstrip()

    if question.isdecimal(): # 자연수라면
        result.append(pokemon_list[int(question)-1])
    else: # 문자라면
        result.append(pokemon[question])

for i in result:
    print(i)