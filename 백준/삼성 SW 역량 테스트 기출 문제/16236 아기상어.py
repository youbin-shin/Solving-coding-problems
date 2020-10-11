def distance(f, s): # 물고기 f와 상어 s 와의 최단 거리를 구하는 함수
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = [[f[0], f[1]]]
    water[s[0]][s[1]] = 0
    visited = [[0]*N for _ in range(N)]
    visited[f[0]][f[1]] = 1
    while q:
        y, x = q.pop(0)
        if [y, x] == [s[0], s[1]]:
            return visited[y][x] -1
        for d in range(4):
            ny = y + dirs[d][0]
            nx = x + dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N:
                if water[ny][nx] <= s[2] and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1


# 입력받기
N = int(input())
water = [list(map(int, input().split())) for _ in range(N)]

fish = []
for i in range(N):
    for j in range(N):
        if water[i][j] == 9:
            shark = [i, j, 2] # 상어 위치, 크기 저장
        elif water[i][j]:
            fish.append([i, j, water[i][j]]) # 물고기 위치, 크기 순으로 저장
cnt = 0 # 몇마리 먹었는지 카운트를 저장할 변수
time = 0
while True:
    eat_fish = []
    for f in range(len(fish)):
        if fish[f][2] < shark[2]: # 아기상어보다 작은 물고기(먹을 수 있는 물고기) 찾기
            d = distance(fish[f], shark) # 물고기와 아기상어와의 최단거리 계산
            if d != None: # 크기가 작더라도 갈 수 없어 None을 return 할 수 있기에 분기 처리 필요(안할 경우 런타임에러)
                eat_fish.append([d] + fish[f])
    if len(eat_fish) == 0:
        break
    eat_fish.sort() # [거리, 물고기 위치y, 물고기 위치x, 크기] 작은 순으로 정렬
    pick_fish = eat_fish[0] # 아기상어가 먹을 고기
    cnt += 1
    water[pick_fish[1]][pick_fish[2]] = 0 # 먹었으니 water 0으로 바꾸기
    fish.pop(fish.index([pick_fish[1], pick_fish[2], pick_fish[3]])) # 먹은 물고기이기에 물고기 리스트에서 삭제
    shark[0], shark[1] = pick_fish[1], pick_fish[2] # 상어 위치 변경
    if cnt == shark[2]:
        shark[2] += 1
        cnt = 0
    time += pick_fish[0]

print(time)