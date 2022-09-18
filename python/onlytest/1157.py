word = input("")
up_word = word.upper()
cnt_word = list(set(up_word))

max_c = []

for i in cnt_word:
    max_c.append(up_word.count(i))

if max_c.count(max(max_c)) > 1:
    print("?")
else:
    print(cnt_word[max_c.index(max(max_c))])
