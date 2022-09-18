import sys

def dfs(l, y, x,):
    l[y][x] = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= len(l) or nx < 0 or nx >= len(l[0]):
            continue
        if l[ny][nx] != 1:
            continue
        dfs(l, ny, nx)
    
    # top_y = y - 1
    # top_x = x
    # right_y = y
    # right_x = x + 1
    # bottom_y = y + 1
    # bottom_x = x
    # left_y = y
    # left_x = x -1
    # if top_y < 0 or top_y >= len(l) or top_x < 0 or top_x >= len(l[0]):
    #     pass
    # else:
    #     if l[top_y][top_x] == 1:
    #         dfs(l, top_y, top_x)
    # if right_y < 0 or right_y >= len(l) or right_x < 0 or right_x >= len(l[0]):
    #     pass
    # else:
    #     if l[right_y][right_x] == 1:
    #         dfs(l, right_y, right_x)
    # if bottom_y < 0 or bottom_y >= len(l) or bottom_x < 0 or bottom_x >= len(l[0]):
    #     pass
    # else:
    #     if l[bottom_y][bottom_x] == 1:
    #         dfs(l, bottom_y, bottom_x)
    # if left_y < 0 or left_y >= len(l) or left_x < 0 or left_x >= len(l[0]):
    #     pass
    # else:
    #     if l[left_y][left_x] == 1:
    #         dfs(l, left_y, left_x)


t = int(sys.stdin.readline())
for tc in range(t):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    l = [[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x, y = list(map(int, sys.stdin.readline().split()))
        l[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                cnt += 1
                dfs(l, i, j)

    print(cnt)