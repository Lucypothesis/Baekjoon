def solution(n):
    lst = [[0] * n for _ in range(n)]
    move = [[0,1],[1,0],[0,-1],[-1,0]]

    x, y = 0, 0
    a, i = 1, 0
    lst[0][0] = a
    a += 1

    for _ in range(n * n - 1):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 방향 변경
            i = (i + 1) % 4
            x += move[i][0]
            y += move[i][1]

        lst[x][y] = a
        a += 1
    return lst