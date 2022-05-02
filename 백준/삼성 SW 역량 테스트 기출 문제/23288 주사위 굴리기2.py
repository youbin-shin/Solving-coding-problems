def get_score_board():
    global N, M
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for y in range(N):
        for x in range(M):
            if score_board[y][x] == 0:
                num = board[y][x]
                same_num = [[y, x]]
                q = [[y, x]]
                visited = [[0] * M for _ in range(N)]
                visited[y][x] = 1
                while q:
                    my, mx = q.pop()
                    for d in range(4):
                        ny, nx = my + dirs[d][0], mx + dirs[d][1]
                        if (
                                0 <= ny < N
                                and 0 <= nx < M
                                and visited[ny][nx] == 0
                                and board[my][mx] == board[ny][nx]
                        ):
                            q.append([ny, nx])
                            visited[ny][nx] = 1
                            same_num.append([ny, nx])
                for sy, sx in same_num:
                    score_board[sy][sx] = len(same_num) * num


def move_dice(dice_d):
    if dice_d == 0:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif dice_d == 1:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif dice_d == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    else:  # dice_d == 3
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score_board = [[0] * M for _ in range(N)]
get_score_board()

dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]
dice_dirs = [0, 1, 2, 3] # 동 남 서 북
dice_d = 0
y, x = 0, 0
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

final_score = 0


for _ in range(K):
    # 1. 주사위가 이동할 칸 없을 경우 반대 방향으로 변경
    ny, nx = y + dirs[dice_d][0], x + dirs[dice_d][1]
    if not 0 <= ny < N or not 0 <= nx < M:
        dice_d = (dice_d + 2) % 4
        ny, nx = y + dirs[dice_d][0], x + dirs[dice_d][1]
    y, x = ny, nx

    move_dice(dice_d)
    # 2. 점수 획득
    final_score += score_board[y][x]
    # 3. 이동할 방향 결정
    dice_num = dice[3][1]
    board_num = board[y][x]
    if dice_num > board_num:
        # 시계 방향 90도 회전
        dice_d = (dice_d + 1) % 4
    elif dice_num < board_num:
        # 반시계 방향 90도 회전
        dice_d = (dice_d + 3) % 4

print(final_score)
