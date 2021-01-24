def blueMove(y, x, h, hd, temp, left): # 파란칸인 경우 동작하는 함수
    # 방향 반대로 바꾸기
    if hd % 2:  # 홀수인 경우
        bh = hd - 1
    else: # 짝수인 경우
        bh = hd + 1
    horse_board[y][x][h][1] = bh

    by, bx = y + dirs[bh][0], x + dirs[bh][1] # 방향 반대로 저장하기
    if 0 <= by < N and 0 <= bx < N:
        # 이동하려는 곳이 흰색인 경우
        if board[by][bx] == 0:
            horse_board[by][bx].extend(temp)
            horse_board[y][x] = left
        # 이동하려는 곳이 빨간색인 경우
        elif board[by][bx] == 1:
            horse_board[by][bx].extend(temp[::-1])
            horse_board[y][x] = left


# 입력받기
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 색을 저장하는 리스트
horse_board = [[[] for _ in range(N)] for _ in range(N)] # 말의 위치를 저장할 리스트

dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]] # 오른쪽, 왼쪽, 위, 아래

for k in range(K):
    r, c, d = map(int, input().split())
    r, c, d = r - 1, c - 1, d - 1
    horse_board[r][c].append([k, d])

answer = -1
cnt = 1 # 게임의 턴을 저장할 변수
frag = False  # 턴이 종료되는 조건이 될 변수
while True:
    if cnt >= 1000: break # 종료조건
    if frag: break
    for k in range(K):
        find = False # 말 위치 찾으면 다음 말 위치 찾을 수 있도록 하는 변수
        if frag: break
        for y in range(N):
            if find: break
            if frag: break
            for x in range(N):
                if find: break
                if frag: break
                if horse_board[y][x] != []:
                    for h in range(len(horse_board[y][x])):
                        if horse_board[y][x][h][0] == k:
                            find = True # 해당하는 말 번호 찾았기에 체크
                            hd = horse_board[y][x][h][1] # 말 방향 저장하는 변수
                            ny, nx = y + dirs[hd][0], x + dirs[hd][1]
                            temp = horse_board[y][x][h:] # 이동할 말 포함하여 위에 있는 말 저장하는 리스트
                            left = horse_board[y][x][:h] # 이동할 말 밑에 있는 말 저장하는 리스트

                            if 0 <= ny < N and 0 <= nx < N:
                                if board[ny][nx] == 0: # 체스판이 흰색인 경우
                                    horse_board[ny][nx].extend(temp)
                                    horse_board[y][x] = left
                                elif board[ny][nx] == 1: # 체스판이 빨간색인 경우
                                    horse_board[ny][nx].extend(temp[::-1])
                                    horse_board[y][x] = left

                                else: # 체스판이 파란색인 경우
                                    blueMove(y, x, h, hd, temp, left)
                            else: # 체크판 벗어나는 경우: 체스판이 파란색인 경우
                                blueMove(y, x, h, hd, temp, left)

                            # 각 말 이동마다 체스판 위에 말이 4개 이상 있는지 확인하기
                            for cy in range(N):
                                if frag: break
                                for cx in range(N):
                                    if len(horse_board[cy][cx]) >= 4:
                                        answer = cnt # 턴 저장하기
                                        frag = True # 종료시키기
                                        break
                            break
    cnt += 1

print(answer)
