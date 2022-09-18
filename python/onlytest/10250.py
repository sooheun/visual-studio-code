from ast import Num
from turtle import width


count = int(input(""))

Height = 0
width = 0
num = 0

answers = []

for i in range(0, count):
    Height, width, num = map(int, input("").split())

    if num % Height == 0:
        answers.append("{0}{1:0>2}".format((Height),(num // Height)))
    else:
        answers.append("{0}{1:0>2}".format((num % Height),(num // Height) + 1))

for i in answers:
    print(i)