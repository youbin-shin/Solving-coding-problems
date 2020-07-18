def clean_up(x, y, cleaner, d):
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    nx = x + dir[d][0]
    ny = y + dir[d][1]
    if after[nx][ny] == -1:
        after[x][y] = 0
        return
    after[x][y] = after[nx][ny]
    wall = [[0, 0], [0, C-1], [cleaner, C-1]]
    if [nx, ny] in wall:
        d += 1
    clean_up(nx, ny, cleaner, d)

def clean_down(x, y, cleaner, d):
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    nx = x + dir[d][0]
    ny = y + dir[d][1]
    if after[nx][ny] == -1:
        after[x][y] = 0
        return
    after[x][y] = after[nx][ny]
    wall = [[R-1, 0], [R-1, C-1], [cleaner, C-1]]
    if [nx, ny] in wall:
        d += 1
    clean_down(nx, ny, cleaner, d)


# 입력을 받는다.
R, C, T = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(R)]
for r in range(R):
    if original[r][0] == -1:
        cleaner = r # 공기 청전기 위치를 찾는다.
        break

for t in range(T):
    after = [[0]*C for _ in range(R)] # 확산이 일어난 상태를 저장할 리스트이다.
    # 공기청정기 위치 저장한다.
    after[r][0] = -1
    after[r+1][0] = -1

    # 확산 진행
    for x in range(R):
        for y in range(C):
            if original[x][y] > 0:
                dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                num = int(original[x][y] / 5)
                cnt = 0
                for d in range(4):
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]
                    if 0 <= nx < R and 0 <= ny < C and after[nx][ny] >= 0:
                        after[nx][ny] += num
                        cnt += 1
                after[x][y] += original[x][y] - num * cnt

    # 공기청정기 작동
    clean_up(cleaner-1, 0, cleaner, 0)
    clean_down(cleaner+2, 0, cleaner+1, 0)
    for i in range(R):
        for j in range(C):
            original[i][j] = after[i][j]

dusts = 0
for x in range(R):
    for y in range(C):
        if original[x][y] > 0:
            dusts += original[x][y]

print(dusts)