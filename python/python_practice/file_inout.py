score_file = open("score.txt", "w", encoding="utf8") # w : 덮어쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a : 수정하기
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r : 읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print("")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
print("")
for line in lines:
    print(line, end="")

score_file.close()