def divide(x, y, d1, d2):
  global answer
  area_people = [0] * 5 # 각 선거구 인원을 저장할 리스트
  visited = [[0] * (N + 1) for _ in range(N + 1)] # x, y, d1, d2를 기준으로 선거구 번호 저장할 리스트
  # 경계선 5구역으로 체크하기
  for i in range(d1+1): 
    nx, ny = x + i, y - i
    visited[nx][ny] = 5
    nx3, ny3 = x + d2 + i, y +d2 - i
    visited[nx3][ny3] = 5
  for i2 in range(d2+1):
    nx2, ny2 = x + i2, y + i2
    visited[nx2][ny2] = 5
    nx4, ny4 = x + d1 + i2, y - d1 + i2
    visited[nx4][ny4] = 5

  # 1번 선거구 표시
  for r1 in range(1, x + d1):
      for c1 in range(1, y + 1):
          if visited[r1][c1] == 5:
              break
          else:
              visited[r1][c1] = 1
  # 2번 선거구 표시
  for r2 in range(1, x + d2 + 1):
      for c2 in range(N, y, -1):
          if visited[r2][c2] == 5:
              break
          else:
              visited[r2][c2] = 2
  # 3번 선거구 표시
  for r3 in range(x + d1, N + 1):
      for c3 in range(1, y - d1 + d2):
          if visited[r3][c3] == 5:
              break
          else:
              visited[r3][c3] = 3
  # 4번 선거구 표시
  for r4 in range(x + d2 + 1, N + 1):
      for c4 in range(N, y + d2 - d1 - 1, -1):
          if visited[r4][c4] == 5:
              break
          else:
              visited[r4][c4] = 4
  # 표시된 선거구에 인구 저장하기
  for v1 in range(1, N+1):
      for v2 in range(1, N + 1):
          if visited[v1][v2] == 0: # 5 경계선 안쪽 부분
              area_people[4] += area[v1-1][v2-1]
          else:
              area_people[visited[v1][v2]-1] += area[v1-1][v2-1]
  diff = max(area_people) - min(area_people)

  if diff < answer:
      answer = diff


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

# 기준점이 가능한 범위 정하기
for tx in range(1, N - 1):
  for ty in range(1, N):
    # 가능한 d1, d2 범위 정하기
    for td1 in range(1, ty):
      for td2 in range(1, N - ty + 1):
        if td1 + td2 + tx <= N: # 행이 넘어가지 않을 조건
          divide(tx, ty, td1, td2)


print(answer)