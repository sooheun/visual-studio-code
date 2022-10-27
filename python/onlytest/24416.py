def fibonacci(n):
    f = [1, 1]
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])  # 코드2
    return f[n-1]

cnt = int(input(""))


print(fibonacci(cnt), cnt - 2)