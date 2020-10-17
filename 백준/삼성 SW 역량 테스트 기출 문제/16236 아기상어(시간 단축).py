def find(o, sy, sx, ssize):
  global time, cnt
  # 상어 근처의 물고기 거리와 좌표 구하기
  visited = [[-1] * N for _ in range(N)]
  q = [[sy, sx]]
  visited[sy][sx] = 0
  temp = []
  min = float('inf')
  while q:
    y, x = q.pop(0)
    if visited[y][x] > min: break # 최단 거리에 있는 물고리 거리, 좌표만 저장
    for d in range(4):
      ny, nx = y + dirs[d][0], x + dirs[d][1]
      if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and o[ny][nx] <= ssize:
        visited[ny][nx] = visited[y][x] + 1
        q.append([ny, nx])
        if o[ny][nx] != 0 and o[ny][nx] < ssize:
          temp.append([visited[ny][nx], ny, nx])
          if visited[ny][nx] < min:
            min = visited[ny][nx]

  if len(temp): # 근처에 물고기가 있는 경우
    temp.sort() # 같은 거리일 경우 가장 좌측 상단인 물고기 선택하기 위한 정렬
    eat_fish_y, eat_fish_x = temp[0][1], temp[0][2]
    o[eat_fish_y][eat_fish_x] = 0 # 물고기 먹기
    time += temp[0][0] # 이동 거리만큼 time 더하기
    cnt += 1
    if cnt == ssize:
      ssize += 1
      cnt = 0
    find(o, eat_fish_y, eat_fish_x, ssize)

  else: # 먹을 물고기가 없는 경우 (종료 조건)
    return




N = int(input())
time = 0
cnt = 0
ocean = []
for i in range(N):
  row = list(map(int, input().split()))
  if row.count(9):
    sh_y, sh_x, sh_size = i, row.index(9), 2
  ocean.append(row)

ocean[sh_y][sh_x] = 0 # 상어 위치 0으로 초기화
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
find(ocean, sh_y, sh_x, sh_size)
print(time)