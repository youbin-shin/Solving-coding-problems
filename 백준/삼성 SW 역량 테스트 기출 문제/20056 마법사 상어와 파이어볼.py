from copy import deepcopy

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

# board에 상어가 있는 경우 [m, s, d] 로 저장하기
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    if m != 0:
        board[r - 1][c - 1].append([m, s, d])

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(K):
    n_board = [[[] for _ in range(N)] for _ in range(N)]

    # 1. 모든 파이어볼이 이동한다.
    for y in range(N):
        for x in range(N):
            if board[y][x] != []:
                for b in range(len(board[y][x])):
                    nm, ns, nd = board[y][x][b]
                    ny, nx = y + dirs[nd][0] * ns, x + dirs[nd][1] * ns
                    nx = (nx + N) % N
                    ny = (ny + N) % N
                    n_board[ny][nx].append([nm, ns, nd])

    # 2. 2개 이상의 파이어볼이 있는 칸을 찾아 4개의 파이어볼을 만든다.
    for y2 in range(N):
        for x2 in range(N):
            if len(n_board[y2][x2]) > 1:
                cm, cs, cd = 0, 0, []
                cnt = len(n_board[y2][x2])
                for c in range(cnt):
                    cm += n_board[y2][x2][c][0]
                    cs += n_board[y2][x2][c][1]
                    cd.append(n_board[y2][x2][c][2] % 2)
                cm = int(cm / 5)
                cs = int(cs / cnt)
                n_board[y2][x2] = []
                if cm != 0: # 질량이 0 인 경우 소멸하는 조건 고려
                    if sum(cd) == 0 or sum(cd) == cnt: # 합쳐지는 파이어볼 방향이 모두 홀수거나 짝수인 경우
                        for i in range(4):
                            n_board[y2][x2].append([cm, cs, i * 2])
                    else:
                        for j in range(4):
                            n_board[y2][x2].append([cm, cs, j * 2 + 1])

    board = deepcopy(n_board)

# 남아있는 파이어볼 질량의 합 구하기
sum_m = 0
for y in range(N):
    for x in range(N):
        if board[y][x] != []:
            for b in range(len(board[y][x])):
                sum_m += board[y][x][b][0]
print(sum_m)
