def fishing(person, ocean):
    global catch
    # 사람 도착지점에 있을 경우 종료
    if person == X: 
        return
    else:
        # 상어잡기
        for i in range(Y):
            if ocean[i][person]: # 같은 열에 상어 발견하면 잡기
                catch += ocean[i][person][2] 
                ocean[i][person] = 0
                break

        # 상어 이동
        next_ocean = [[0] * X for _ in range(Y)]
        for y in range(Y):
            for x in range(X):
                if ocean[y][x] != 0: # 상어가 있을 경우
                    ny, nx, v, d, z = y, x, ocean[y][x][0], ocean[y][x][1], ocean[y][x][2]
                    # 이동이 제자리로 오는 경우 카운트 제외하기 위해 (X -1) * 2로 나누기
                    if d == 1 or d == 2:
                        move = v % ((Y - 1) * 2)
                    else:
                        move = v % ((X - 1) * 2)
                    while move: # 하나씩 이동시키기
                        if d == 1:
                            if ny == 0:
                                d = 2
                            ny += dirs[d][0]
                            if ny == 0:
                                d = 2
                        elif d == 2:
                            if ny == Y-1:
                                d = 1
                            ny += dirs[d][0]
                            if ny == Y-1:
                                d = 1
                        elif d == 3:
                            if nx == X-1:
                                d = 4
                            nx += dirs[d][1]
                            if nx == X-1:
                                d = 4
                        elif d == 4:
                            if nx == 0:
                                d = 3
                            nx += dirs[d][1]
                            if nx == 0:
                                d = 3
                        move -= 1
                    if next_ocean[ny][nx]: # 상어가 있을 경우 크기 비교하기
                        if next_ocean[ny][nx][2] < z:
                            next_ocean[ny][nx] = [v, d, z]
                    else: # 상어가 없을 경우 저장
                        next_ocean[ny][nx] = [v, d, z]
        fishing(person + 1, next_ocean)

Y, X, M = map(int, input().split())
ocean_init = [[0] * X for _ in range(Y)]
dirs = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
catch = 0
for _ in range(M):
    y, x, v, d, z = map(int, input().split())
    ocean_init[y-1][x-1] = [v, d, z]
fishing(0, ocean_init)
print(catch)
