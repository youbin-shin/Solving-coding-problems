from copy import deepcopy
def gravity(board, N):
    for x in range(N):
        for y in range(N - 1, -1, -1):
            if board[y][x] not in [-1, 'x']:
                val = board[y][x]
                board[y][x] = 'x'
                check_y = y
                while True:
                    if check_y == N - 1:
                        board[check_y][x] = val
                        break
                    mov_y = check_y + 1
                    if board[mov_y][x] != 'x':
                        board[check_y][x] = val
                        break
                    check_y = mov_y


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

final_score = 0
while True:
    block_group = []
    visited = [[0] * N for _ in range(N)]
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    # 블록 그룹 찾기
    for y in range(N):
        for x in range(N):
            if board[y][x] not in ['x', 0, -1] and visited[y][x] == 0:
                visited[y][x] = 1
                color = board[y][x]
                rainbow = 0
                row_num = y
                col_num = x
                block = [[y, x]]
                q = [[y, x]]
                cnt = 1
                while q:
                    my, mx = q.pop(0)
                    for d in range(4):
                        ny, nx = my + dirs[d][0], mx + dirs[d][1]
                        if 0 <= ny < N and 0 <= nx < N:
                            if board[ny][nx] == color and visited[ny][nx] == 0:
                                block.append([ny, nx])
                                q.append([ny, nx])
                                visited[ny][nx] = 1
                                cnt += 1
                                if ny < row_num:
                                    row_num = ny
                                    col_num = nx
                                elif ny == row_num and nx < col_num:
                                    col_num = nx
                            elif board[ny][nx] == 0:
                                if [ny, nx] not in block:
                                    block.append([ny, nx])
                                    q.append([ny, nx])
                                    rainbow += 1
                                    cnt += 1

                if cnt >= 2:
                    blocks = [len(block), rainbow, row_num, col_num, block]
                    block_group.append(blocks)
    if block_group == []: break
    big_block_group = sorted(block_group, key=lambda x : (-x[0], -x[1], -x[2], -x[3]))
    big_block_group = big_block_group[0]
    final_score += big_block_group[0] * big_block_group[0]
    remove_block = big_block_group[4]
    for b in remove_block:
        board[b[0]][b[1]] = 'x'
    gravity(board, N)

    next_board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            next_board[y][x] = board[x][N - y - 1]
    board = deepcopy(next_board)
    gravity(board, N)
print(final_score)