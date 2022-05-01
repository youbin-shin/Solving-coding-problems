"""
디버깅 히스토리
1. 예제 5, 6이 틀린 경우 
    재방문할 수 없도록 로직으로 인해 문제에 재방문이 불가능하다는 조건은 없다.
2. 제출 실패 이유
    처음 상어 위치를 방문 처리하고 시작하면 안된다.
    [관련 테스트 케이스 (정답: 23, 오답: 30)]
    16 3
    1 1 1
    1 1 2
    1 1 3
    1 1 4
    1 1 5
    1 1 6
    1 1 7
    1 1 8
    2 1 1
    2 1 2
    2 1 3
    2 1 4
    2 1 5
    2 1 6
    2 1 7
    2 1 8
    2 1
"""


def move_shark(i, die_fish_cnt, die_fish_list, y, x, visited):
    global n_board, N, max_die_fish_cnt, max_die_fish_list, sy, sx
    s_dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    if i == 3:
        if max_die_fish_cnt < die_fish_cnt:
            max_die_fish_cnt = die_fish_cnt
            max_die_fish_list = die_fish_list
            sy, sx = y, x
        return
    # 아래 주석 로직: 처음 상어 위치 방문 처리한 로직 (실패 원인)
    # if i == 0:
    #     visited[y][x] = 1
    #     if n_board[y][x] != 0 and visited[y][x] == 0:
    #         die_fish_list.append([y, x])
    #         die_fish_cnt += len(n_board[y][x])
    for d in range(4):
        ny, nx = y + s_dirs[d][0], x + s_dirs[d][1]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if n_board[ny][nx] != 0:
                    n_die_fish_list = die_fish_list + [[ny, nx]]
                    n_die_fish_cnt = die_fish_cnt + len(n_board[ny][nx])
                    move_shark(i + 1, n_die_fish_cnt, n_die_fish_list, ny, nx, visited)
                visited[ny][nx] = 0
                move_shark(i + 1, die_fish_cnt, die_fish_list, ny, nx, visited)
            else:
                move_shark(i + 1, die_fish_cnt, die_fish_list, ny, nx, visited)


N = 4
M, S = map(int, input().split())
fish_info = [list(map(int, input().split())) for _ in range(M)]
sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1

fish_smell_board = [[0] * N for _ in range(N)]
board = [[0] * N for _ in range(N)]
for fy, fx, fd in fish_info:
    if board[fy - 1][fx - 1] == 0:
        board[fy - 1][fx - 1] = [fd - 1]
    else:
        board[fy - 1][fx - 1].append(fd - 1)
n_board = [[0] * N for _ in range(N)]


dirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
for s in range(S):
    # 1. 물고기 복제 마법 시작 (위치 기록)
    # 2. 물고기 한칸씩 이동
    previous_fish_info = []
    n_board = [[0] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                for d in board[y][x]:
                    previous_fish_info.append([y, x, d])
                    for i in range(9):
                        ny, nx = y + dirs[d][0], x + dirs[d][1]
                        # 이동할 수 있는 조건
                        if 0 <= ny < N and 0 <= nx < N and [ny, nx] != [sy, sx] and fish_smell_board[ny][nx] == 0:
                            if n_board[ny][nx] == 0:
                                n_board[ny][nx] = [d]
                            else:
                                n_board[ny][nx].append(d)

                            break
                        elif i == 8: # 움직일 곳이 없어 자리 이동 안함
                            if n_board[y][x] == 0:
                                n_board[y][x] = [d]
                            else:
                                n_board[y][x].append(d)
                            break
                        d = (d - 1) % 8

    # 3. 상어 이동
    max_die_fish_cnt = -1
    max_die_fish_list = []
    move_shark(0, 0, [], sy, sx, [[0] * N for _ in range(N)])

    # 4. 물고기 냄새 업데이트 (2번 전 연습 냄새 사라짐)
    for r in range(N):
        for c in range(N):
            if fish_smell_board[r][c] != 0:
                fish_smell_board[r][c] -= 1
    for dfy, dfx in max_die_fish_list:
        n_board[dfy][dfx] = 0
        fish_smell_board[dfy][dfx] = 2

    # 5. 물고기 복제 마법 발동
    for nfy, nfx, nfd in previous_fish_info:
        if n_board[nfy][nfx] == 0:
            n_board[nfy][nfx] = [nfd]
        else:
            n_board[nfy][nfx].append(nfd)
    board = n_board


# 물고기 수 확인
answer = 0
for r in range(N):
    for c in range(N):
        if board[r][c] != 0:
            answer += len(board[r][c])
print(answer)
