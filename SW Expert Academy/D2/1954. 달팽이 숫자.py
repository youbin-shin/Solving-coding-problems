def move(x, y, status, N):
    if status == 0:
        if y == N-1:
            status += 1
        elif board[x][y+1] != 0:
            status += 1
        else:
            status = 0
    elif status == 1:
        if x == N-1:
            status += 1
        elif board[x+1][y] != 0:
            status += 1
        else:
            status = 1
    elif status == 2:
        if y == 0:
            status += 1
        elif board[x][y-1] != 0:
            status += 1
        else:
            status = 2
    else:
        if x == 0:
            status = 0
        elif board[x-1][y] != 0:
            status = 0
        else:
            status = 3

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x += dx[status]
    y += dy[status]

    return x, y, status


T = int(input())

for tc in range(T):
    print('#{}'.format(tc+1))
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

    x = y = 0
    direction = 0
    for i in range(1, N*N+1):
        board[x][y] = i
        x, y, direction = move(x, y, direction, N)

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()