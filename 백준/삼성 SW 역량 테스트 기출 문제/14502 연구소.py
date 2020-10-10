from itertools import combinations
from copy import deepcopy

def spread(test_area): # 바이러스 확사시키는 함수
    global final_cnt
    q = []
    for y in range(Y):
        for x in range(X):
            if test_area[y][x] == 2: # 바이러스가 있는 좌표 저장
                q.append([y, x])
    while q: # 바이러스 퍼지는 동작 수행
        ty, tx = q.pop()
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for d in range(4):
            ny, nx = ty + dirs[d][0], tx + dirs[d][1]
            if 0 <= ny < Y and 0 <= nx < X:
                if test_area[ny][nx] == 0:
                    q.append([ny, nx])
                    test_area[ny][nx] = 2
    cnt = 0
    for y2 in range(Y):
        for x2 in range(X):
            if test_area[y2][x2] == 0: # 바이러스가 없는 좌표 카운트
                cnt += 1
    if final_cnt < cnt:
        final_cnt = cnt



def make_wall(w): # 벽 만들어주는 함수
    test_area = deepcopy(area)
    for i in w:
        test_area[i[0]][i[1]] = 1 # 벽세우기
    spread(test_area) # 3개의 벽을 세운 뒤 바이러스 확산하기


# 입력받기
Y, X = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(Y)]

final_cnt = 0 # 최종 출력을 저장할 변수
empty_area = [] # 빈칸 0 인 좌표 저장할 리스트
for y in range(Y):
    for x in range(X):
        if area[y][x] == 0:
            empty_area.append([y, x])

# 빈칸 좌표 중 조합으로 3개를 뽑는 경우를 모두 저장하기
wall_list = list(combinations(empty_area, 3))
for w in wall_list: # 조합 중 하나씩 벽 세우기
    make_wall(w)

print(final_cnt)