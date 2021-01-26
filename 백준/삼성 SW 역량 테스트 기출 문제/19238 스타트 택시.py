from collections import deque

def findPassenger(taxi): # 최단 경로의 손님을 찾는 함수
    q = deque()
    q.append(taxi)
    visited = [[0] * N for _ in range(N)]
    minDistance = float('inf')
    candidate = [] # 최단 경로인 승객들을 저장할 리스트
    while q: # BFS를 이용하여 최단 경로 탐색하기
        y, x = q.popleft()
        if visited[y][x] > minDistance:
            break
        if [y, x] in passenger_start: # 최단 경로 손님 찾기
            minDistance = visited[y][x]
            candidate.append([y, x])
        else:
            for d in range(4):
                ny, nx = y + dirs[d][0], x + dirs[d][1]
                if 0 <= ny < N and 0 <= nx < N and road[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
    if candidate:
       candidate.sort() # 최단 경로, 행, 열를 기준으로 오름차순으로 정렬하기
       return visited[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]
    else: # 손님한테 갈 수 없는 경우
       return -1, -1, -1

def goDestination(start, end): # 손님의 목적지로 가는 함수
    q = deque()
    q.append(start)
    visited = [[0] * N for _ in range(N)]
    while q: # BFS를 이용하여 최단 경로 탐색하기
        y, x = q.popleft()
        if [y, x] == end:
            break
        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N and road[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
    return visited[y][x], y, x

# 입력받기
N, M, fuel = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
taxi = [ty - 1, tx - 1]

passenger_start = [] # 손님들의 출발지를 저장할 리스트
passenger_end = [] # 손님들의 도착지를 저장할 리스트
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    passenger_start.append([sy - 1, sx - 1])
    passenger_end.append([ey - 1, ex - 1])
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for _ in range(M):
    distance, py, px = findPassenger(taxi) # 최단 경로의 손님을 찾는 함수
    if distance == -1 or fuel - distance < 0: # 손님에게 못가거나 연료가 떨어지는 종료조건
        fuel = -1
        break
    fuel -= distance # 손님한테 가는 길에 사용한 연료 계산하기
    idx = passenger_start.index([py, px]) # 최단 경로의 손님의 인덱스 찾기
    passenger_start[idx] = [-1, -1] # 손님을 태웠기에 findPassenger에서 제외되기 위해 [-1, -1]로 설정하기
    distance2, py2, px2 = goDestination([py, px], passenger_end[idx]) # 손님의 목적지로 가는 함수
    if [py2, px2] != passenger_end[idx] or fuel - distance2 < 0: # 도착지에 도달하지 못하거나 연료가 떨어지는 종료조건
        fuel = -1
        break
    # 손님을 도착지에 잘 데려다준 경우
    fuel += distance2 # 도착지까지 연료를 - distance 사용하고 충전이 + distance * 2 이기에 최종적으로 + distance하기
    taxi = [py2, px2] # 택시 위치 갱신하기


print(fuel)