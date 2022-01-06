N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

final_sum = 0
dirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
for m in range(M):
    visited = [[False] * N for _ in range(N)]
    magic = []
    for c in clouds:
        y, x = c[0], c[1]
        y = (y + dirs[moves[m][0] - 1][0] * moves[m][1]) % N
        x = (x + dirs[moves[m][0] - 1][1] * moves[m][1]) % N
        board[y][x] += 1
        visited[y][x] = True
        magic.append([y, x])
    magic_dirs = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for m in magic:
        my, mx = m[0], m[1]
        cnt = 0
        for d in range(4):
            nmy, nmx = my + magic_dirs[d][0], mx + magic_dirs[d][1]
            if 0 <= nmy < N and 0 <= nmx < N and board[nmy][nmx] > 0:
                cnt += 1
        board[my][mx] += cnt
    clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not visited[i][j]:
                clouds.append([i, j])
                board[i][j] -= 2

for i in range(N):
    final_sum += sum(board[i])

print(final_sum)