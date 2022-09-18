word = input("")
count = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in count:
    word = word.replace(i, "_")

print(len(word))