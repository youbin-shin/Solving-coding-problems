city_num = int(input())

city_map = [[float('inf')] * city_num for _ in range(city_num)]
for _ in range(int(input())):
  start, end, expense = map(int, input().split())
  city_map[start - 1][end - 1] = min(expense, city_map[start - 1][end - 1])
for c in range(city_num):
  city_map[c][c] = 0
for i in range(city_num): # 경유지
  for s in range(city_num): # 출발지
    for e in range(city_num): # 도착지
      # 출발지 ~ 도착지, 출발지 ~ 경유지 + 경유지 ~ 도착지 의 최소값 저장
      city_map[s][e] = min(city_map[s][e], city_map[s][i] + city_map[i][e])

# 무한대일 경우 0으로 바꾸기
for f1 in range(city_num):
  for f2 in range(city_num):
    if city_map[f1][f2] == float('inf'):
      city_map[f1][f2] = 0

for l in range(city_num):
  print(" ".join(map(str, city_map[l])))