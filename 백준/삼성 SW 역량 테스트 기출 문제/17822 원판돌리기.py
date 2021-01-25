from copy import deepcopy

N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(N)]
rotate = [list(map(int, input().split())) for _ in range(T)]

for t in range(T):
    # 1. x의 배수인 원판을 d 만큼 k 칸 회전 시키기
    x, d, k = rotate[t]
    xx = x
    while xx <= N:
        if d == 0:  # 시계 방향
            circles[xx - 1] = circles[xx - 1][-k:] + circles[xx - 1][:-k]
        else:  # 반시계 방향
            circles[xx - 1] = circles[xx - 1][k:] + circles[xx - 1][:k]
        xx += x

    n_circles = [[-1] * M for _ in range(N)]
    # 2. 원판의 수가 있는 경우 인접한 수 탐색하기
    # 2-1. 인접한 수가 서로 같으면 모두 0으로 지운다.
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    no_change = True # 인접한 수가 없었는지 기준이 되는 변수
    for y in range(N):
        for x in range(M):
            if circles[y][x] > 0:
                q = [[y, x]]
                while q:
                    qy, qx = q.pop(0)
                    for d in range(4):
                        ny, nx = qy + dirs[d][0], qx + dirs[d][1]
                        nx = (nx + M) % M # 원판 => 행의 인덱스 0번이랑 마지막 번이 이어져 있음을 고려
                        if 0 <= ny < N and circles[y][x] == circles[ny][nx] and n_circles[ny][nx] == -1:
                            n_circles[y][x] = 0
                            n_circles[ny][nx] = 0
                            q.append([ny, nx])
                            if no_change: no_change = False
                if n_circles[y][x] == -1: # 인접하지 않은 수이기에 원래 값 저장하기
                    n_circles[y][x] = circles[y][x]
            elif circles[y][x] == 0: # 지워진 수라는 것을 저장하기
                n_circles[y][x] = 0

    # 2-2. 원판에 인접한 수가 없는 경우 새로운 값으로 갱신한다.
    if no_change:
        num_sum = 0
        num_cnt = 0
        change_list = [] # 원판에 적힌 수의 위치를 저장할 리스트
        for y2 in range(N):
            for x2 in range(M):
                if n_circles[y2][x2] > 0:
                    num_sum += n_circles[y2][x2]
                    num_cnt += 1
                    change_list.append([y2, x2])
        if num_cnt != 0: # 조건 필요! (없으면 런타임 에러-ZeroDivisionError 발생)
            num_avg = num_sum / num_cnt
            for c in change_list: # 평균 기준으로 큰 수는 -1, 작은 수는 +1로 값 변경하기
                if n_circles[c[0]][c[1]] > num_avg:
                    n_circles[c[0]][c[1]] -= 1
                elif n_circles[c[0]][c[1]] < num_avg:
                    n_circles[c[0]][c[1]] += 1

    circles = deepcopy(n_circles)

# 최종저긍로 원판에 적힌 수의 합 구하기
final_sum = 0
for i in range(N):
    final_sum += sum(circles[i])
print(round(final_sum))