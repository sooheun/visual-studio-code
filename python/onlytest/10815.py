ccard_cnt = int(input(""))

sang_card = set(map(int, input("").split()))

num_cnt = int(input(""))

num_list = list(map(int, input("").split()))

result = []

def check(i, sang_card):
    if i in sang_card:
        return 1 
    else:
        return 0

for i in num_list:
    print(check(i, sang_card), end=" ")