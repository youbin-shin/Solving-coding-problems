T = 10

for tc in range(T):
    test = int(input())
    board = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    start = []

    for i in range(102):
        if board[0][i] == 1:
            start.append(i)

    result = 1000000
    for s in start:
        cnt = 0
        x = 0
        y = s
        while x < 100:
            while board[x][y+1] == 1:
                y += 1
                cnt += 1
                if board[x][y+1] != 1:
                    x += 1
            while board[x][y-1] == 1:
                y -= 1
                cnt += 1
                if board[x][y-1] != 1:
                    x += 1
            x += 1
            cnt +=1

        if cnt < result:
            result = cnt
            finalresult = s
    print('#{} {}'.format(tc+1, finalresult-1))