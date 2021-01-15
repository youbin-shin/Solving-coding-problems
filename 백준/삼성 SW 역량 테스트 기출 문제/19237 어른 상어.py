from copy import deepcopy

# 입력을 받기
N, M, k = map(int, input().split())
ocean = [[0] * N for _ in range(N)]

temp = [list(map(int, input().split())) for _ in range(N)]
temp_dir = list(map(int, input().split()))

# ocean 리스트에 원하는 형태로 저장하기
# 상어가 있으면 [번호, k, 방향] => 번호, 방향 모두 0부터 시작하도록 설정
# 상어가 없지만 냄새가 남아있다면 [번호, 남은 시간]
# 상어가 없고 냄새도 없다면 0
for i in range(N):
    for j in range(N):
        if temp[i][j] != 0:
            ocean[i][j] = [temp[i][j] - 1, k, temp_dir[temp[i][j] - 1] - 1]

# 상어마다 주어지는 우선순위 방향 저장하기 => 방향 모두 0부터 시작하도록 설정
shark_dir = [] * M
for _ in range(M):
    temp = []
    for t1 in range(4):
        temp.append(list(map(int, input().split())))
        for t2 in range(4):
            temp[t1][t2] -= 1
    shark_dir.append(temp)

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

out = 0 # 상어가 격자 밖으로 쫓겨나는 경우 cnt
time = 0 # 얼마나 지났는지 체크해줄 변수
while out < M - 1:
    if time >= 1000: # 조건 중요!
        time = -1
        break

    time += 1
    next_ocean = [[0] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            # 1. 남아있는 냄새 유지 시간 줄이기
            # 주의 : next_ocean에 상어 있는 경우 건드리면 X
            if ocean[y][x] != 0 and len(ocean[y][x]) == 2 and ocean[y][x][1] > 1:
                if next_ocean[y][x] != 0 and len(next_ocean[y][x]) == 3: # 상어가 있으면 냄새로 없애면 안된다!!
                    pass
                else:
                    next_ocean[y][x] = [ocean[y][x][0], ocean[y][x][1] - 1]

            # 2. 상어 이동시키기
            if ocean[y][x] != 0 and len(ocean[y][x]) == 3: # 상어가 있는 경우
                # 2-1. 현재 자리 냄새 기록하기
                if k - 1 > 0:
                    next_ocean[y][x] = [ocean[y][x][0], k - 1]
                # 2-2. 이동할 자리 탐색하기
                num, sd = ocean[y][x][0], ocean[y][x][2]
                frag = True # 냄새 없는 칸이 없는 경우 true 유지
                frag_temp = []

                for d in range(4):
                    nd = shark_dir[num][sd][d]
                    ny, nx = y + dir[nd][0], x + dir[nd][1]
                    if 0 <= ny < N and 0 <= nx < N and ocean[ny][nx] == 0:
                        frag = False
                        if next_ocean[ny][nx] != 0 and len(next_ocean[ny][nx]) > 2:
                            # 한칸에 두마리 상어가 만난 경우
                            out += 1
                            if next_ocean[ny][nx][0] > num:
                                next_ocean[ny][nx] = [num, k, nd]
                        else:
                            next_ocean[ny][nx] = [num, k, nd]
                        break
                    elif 0 <= ny < N and 0 <= nx < N and ocean[ny][nx] != 0 and ocean[ny][nx][0] == num:
                        frag_temp.append([ny, nx, nd]) # 자신의 냄새가 있는 위치 저장하기
                if frag : # 주위에 빈칸이 없는 경우
                    # 자신 냄새가 있는 칸으로 이동시키기
                    ny, nx, nd = frag_temp.pop(0)
                    if next_ocean[ny][nx] != 0 and len(next_ocean[ny][nx]) > 2:
                        # 한칸에 두마리 상어가 만난 경우
                        out += 1
                        if next_ocean[ny][nx][0] > num:
                            next_ocean[ny][nx] = [num, k, nd]
                    else:
                        next_ocean[ny][nx] = [num, k, nd]

    ocean = deepcopy(next_ocean)

print(time)