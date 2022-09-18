print("Python", "Java", "JavaScript", sep=" , ",end="?")
print("무엇이 재밌을까요?")

scores = {"수학": 0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(4))

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")