from copy import deepcopy

def shark(ocean, new_eat, sy, sx, sd):
  global final_eat
  move_fish(ocean) # 물고기 이동시키기
  eat_list = []
  ocean[sy][sx] = [0, 0]
  nsy, nsx = sy + dirs[sd][0], sx + dirs[sd][1]
  while 0 <= nsy < 4 and 0 <= nsx < 4:
    if ocean[nsy][nsx][0] != 0:
      eat_list.append([nsy, nsx, ocean[nsy][nsx][0], ocean[nsy][nsx][1]])
    nsy, nsx = nsy + dirs[sd][0], nsx + dirs[sd][1]
  if len(eat_list):
    for eat in eat_list:
      red_ocean = deepcopy(ocean)
      red_ocean[eat[0]][eat[1]] = [-1, -1]
      shark(red_ocean, new_eat + eat[2], eat[0], eat[1], eat[3])
  else: # 먹을 물고기가 없는 경우
    if new_eat > final_eat:
      final_eat = new_eat


def move_fish(ocean):
  for num in range(1, 17): # 작은 번호의 물고기 부터 이동시키기
    y, x, d = -1, -1, -1
    frag = False
    for fy in range(4):
      if frag: break
      for fx in range(4):
       if ocean[fy][fx][0] == num:
          frag = True
          y, x = fy, fx
          d = ocean[fy][fx][1]
          break
    if [y, x, d] != [-1, -1, -1]:
      for _ in range(8):
        ny, nx = y + dirs[d][0], x + dirs[d][1]
        if 0 <= ny < 4 and 0 <= nx < 4 and ocean[ny][nx][0] != -1:
          ocean[ny][nx], ocean[y][x] = ocean[y][x], ocean[ny][nx]
          ocean[ny][nx][1] = d
          break
        else: # 이동할 수 없을 경우 방향 바꾸기
          d = (d + 1) % 9
          if d == 0: d = 1


ocean = [[0] * 4 for _ in range(4)]
for i in range(4):
  ab_list = list(map(int, input().split()))
  idx = 0
  for j in range(0, 8, 2):
    ocean[i][idx] = [ab_list[j], ab_list[j+1]]
    idx += 1

sh_y, sh_x, sh_d = 0, 0, ocean[0][0][1]
final_eat = ocean[0][0][0]
ocean[0][0] = [-1, -1]
dirs = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
shark(ocean, final_eat, sh_y, sh_x, sh_d)

print(final_eat)