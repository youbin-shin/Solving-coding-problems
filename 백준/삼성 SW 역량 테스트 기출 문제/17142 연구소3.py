from itertools import combinations
from collections import deque


def spread(virus_list): # 활성화된 바이러스가 퍼지는 시간을 계산하는 함수
    global min_time
    q = deque()
    q.extend(virus_list)
    visited = [[-1] * N for _ in range(N)] # 퍼지는 데 걸린 시간을 저장할 리스트
    complete = 0 # 빈 칸에 퍼뜨리는 경우를 카운트할 변수
    for v in virus_list: # 활성화되는 바이러스 위치를 0으로 설정하기
        visited[v[0]][v[1]] = 0
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while q: # bfs 를 이용하여 퍼뜨리는 시간 계산하기
        y, x = q.popleft()
        if complete == final_complete: # 빈 칸에 모두 다 퍼뜨린 경우
            break
        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N and lab[ny][nx] != 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                if lab[ny][nx] == 0:
                    complete += 1 # 빈 칸에 바이러스가 퍼졌기에 +1 하기
                q.append([ny, nx])
    time = 0
    for i in range(N):
        if time < max(visited[i]):
            time = max(visited[i])
    # 빈 칸을 바이러스로 모두 퍼뜨리고 시간도 최소 시간일 경우 갱신하기
    if complete == final_complete and time < min_time: 
        min_time = time


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = [] # 바이러스들의 위치를 저장할 리스트
wall_cnt = 0 # 벽의 개수

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])
        elif lab[i][j] == 1:
            wall_cnt += 1
final_complete = N * N - len(virus) - wall_cnt  # 바이러스를 퍼지게 해야하는 빈 칸의 수
acive_virus = list(combinations(virus, M)) # 순열을 이용하여 M개의 활성화되는 바이러스 리스트를 만들기 (완전탐색) 
min_time = float('inf')

for a in acive_virus: # 순열 리스트에서 하나씩 확산시키기
    spread(a) # 활성화된 바이러스가 퍼지는 시간을 계산하는 함수

if min_time == float('inf'): # 초기 설정값이 같기에 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우
    min_time = -1
print(min_time)