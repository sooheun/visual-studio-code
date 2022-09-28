def recursion(s,l,r): #ABBA 0 3
    global cnt
    cnt += 1
    if(l >= r):
        return 1
    elif (s[l] != s[r]): 
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

count = int(input(""))

words = [input("") for _ in range(count)]

for i in words:
    cnt = 0
    print(isPalindrome(i), cnt)
