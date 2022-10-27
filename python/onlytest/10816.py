from itertools import count
import sys

def counting_sort(array):
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

now_cnt = int(sys.stdin.readline().rstrip())
now_card = list(map(int, sys.stdin.readline().rstrip().split()))
now_card_dict = {}

now_card_dict = counting_sort(now_card)

q_cnt = int(sys.stdin.readline().rstrip())
q_card = list(map(int, sys.stdin.readline().rstrip().split()))

for i in q_card:
    if i in now_card_dict:
        print(now_card_dict[i], end=" ")
    else:
        print(0, end=" ")