for tc in range(int(input())):
    N, M = map(int, input().split())
    # 1. 시합 전 세팅하기
    board = [[0] * N for _ in range(N)]
    half_N = N // 2
    board[half_N - 1][half_N - 1], board[half_N][half_N] = 2, 2
    board[half_N - 1][half_N], board[half_N][half_N - 1] = 1, 1

    # 2. 플레이 시작 - 돌을 위치에 두고 변화해야할 위치 찾기
    for _ in range(M):
        y, x, color = map(int, input().split())
        y, x = y - 1, x - 1
        board[y][x] = color

        dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for d in range(8): # 가로, 세로, 대각선 모든 부분 탐색하기
            temp = []
            ny, nx = y, x
            change = False # 돌 색이 변하는지 판단하는 변수

            while True:
                ny, nx = ny + dir[d][0], nx + dir[d][1]
                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] != color and board[ny][nx] != 0:
                        temp.append([ny, nx])
                    elif board[ny][nx] == color:
                        if temp != []: # 변화 필요한 경우
                            change = True
                        break
                    else:
                        break
                else:
                    break
            if change: # 변화가 필요한 경우 돌 색 바꾸기
                for t in temp:
                    board[t[0]][t[1]] = color

    # 3. 흑돌, 백돌 세서 출력하기
    black = 0
    white = 0
    for n in range(N):
        black += board[n].count(1)
        white += board[n].count(2)
    print("#{} {} {}".format(tc + 1, black, white))