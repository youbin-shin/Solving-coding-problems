N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** N)]
Q_list = list(map(int, input().split()))

for q in Q_list:
    # 1. 회전하기
    rotate_board = [[0] * (2 ** N) for _ in range(2 ** N)]
    for i in range(0, 2 ** N, 2 ** q):
        for j in range(0, 2 ** N, 2 ** q):
            for i2 in range(2 ** q):
                for j2 in range(2 ** q):
                    rotate_board[i + j2][j + 2 ** q - 1 - i2] = board[i + i2][j + j2]
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 2. 얼음 녹이기
    board = [[0] * (2 ** N) for _ in range(2 ** N)]
    for y in range(2 ** N):
        for x in range(2 ** N):
            cnt = 0
            for d in range(4):
                ny, nx = y + dirs[d][0], x + dirs[d][1]
                if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N and rotate_board[ny][nx] != 0:
                    cnt += 1
            if rotate_board[y][x] > 0:
                if cnt < 3:
                    board[y][x] = rotate_board[y][x] - 1
                else:
                    board[y][x] = rotate_board[y][x]


# 3. 남아있는 얼음 합과 가장 큰 덩어리를 차지하는 칸의 개수 구하기
ice_sum = 0  # 남아있는 얼음 합에 대한 변수
ice_amount_list = [0] # 얼음 덩어리 개수를 저장할 리스트
visited = [[False] * (2 ** N) for _ in range(2 ** N)]
for y in range(2 ** N):
    for x in range(2 ** N):
        temp = []
        if board[y][x] != 0 and visited[y][x] == False:
            temp.append([y, x])
            visited[y][x] = True
            ice_sum += board[y][x]
            cnt = 1
            while temp: 				
                test = temp.pop()
                ty, tx = test[0], test[1]
                for d in range(4):
                    nty, ntx = ty + dirs[d][0], tx + dirs[d][1]
                    if 0 <= nty < 2 ** N and 0 <= ntx < 2 ** N and visited[nty][ntx] == False and board[nty][ntx] != 0:
                        temp.append([nty, ntx])
                        visited[nty][ntx] = True
                        ice_sum += board[nty][ntx]
                        cnt += 1
            ice_amount_list.append(cnt)


print(ice_sum)
print(max(ice_amount_list))