import sys

input = sys.stdin.readline
n = int(input())

words = []

for i in range(n):
    words.append(input().rstrip())

words = list(set(words)) #중복 제거

words.sort() # 알파벳 순 정리
words.sort(key=lambda x: len(x))# 문자수 기준으로 정리

for i in words:
    print(i)