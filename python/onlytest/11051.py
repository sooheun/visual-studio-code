cnt = int(input(""))

for i in range(cnt):
    k, n = map(int, input("").split())
# (n, k) = (n - 1, k - 1) + (n - 1, k) (파스칼의 법칙)
    nums = [[0 for i in range(j)] for j in range(1, n+2)]

    for i in range(1, n + 1): #n C k 에서 n부분 1부터 n 까지 증가
        for j in range(0, i + 1): #n C k에서 k부분 0부터 시작함
            if (i == j or j == 0): # n과 k가 같거나 k가 0이면 n C k = 1임
                nums[i][j] = 1
            else:
                nums[i][j] = nums[i-1][j-1] + nums[i - 1][j]

    print(nums[n][k])
