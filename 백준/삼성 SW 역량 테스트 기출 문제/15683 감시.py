from copy import deepcopy # 사용하지 않을 경우 영향 받음!

def left(ty, tx, room): # 왼쪽 방향으로 감시가능한지 확인하는 함수
  for lx in range(tx-1, -1, -1):
    if room[ty][lx] in cctv_num:
      continue
    elif room[ty][lx] == 6:
      break
    else:
      room[ty][lx] = -1
  return room


def right(ty, tx, room): # 오른쪽 방향으로 감시가능한지 확인하는 함수
  for rx in range(tx+1, X):
    if room[ty][rx] in cctv_num:
      continue
    elif room[ty][rx] == 6:
      break
    else:
      room[ty][rx] = -1
  return room


def up(ty, tx, room): # 위의 방향으로 감시가능한지 확인하는 함수
  for uy in range(ty-1, -1, -1):
    if room[uy][tx] in cctv_num:
      continue
    elif room[uy][tx] == 6:
      break
    else:
      room[uy][tx] = -1
  return room


def down(ty, tx, room): # 밑의 방향으로 감시가능한지 확인하는 함수
  for dy in range(ty+1, Y):
    if room[dy][tx] in cctv_num:
      continue
    elif room[dy][tx] == 6:
      break
    else:
      room[dy][tx] = -1
  return room


def search(lst): # 사각지대 계산하는 함수
  global min_value
  value = 0
  for l in range(Y):
    value += lst[l].count(0)
    if min_value < value:
      return
  if min_value > value:
    min_value = value


def install(n, k, rooms): # cctv 작동시키는 함수
  if n == k: # 존재하는 cctv 개수만큼 고려했을 경우 사각지대 구하기
    search(rooms)

  else:
    num, y, x = cctv_list[n]
    if num == 1: # 1번 cctv 인 경우 총 4가지 경우가 존재
      case1_1 = deepcopy(rooms)
      case1_1 = left(y, x, case1_1)
      install(n + 1, k, case1_1)
      case1_2 = deepcopy(rooms)
      case1_2 = right(y, x, case1_2)
      install(n + 1, k, case1_2)
      case1_3 = deepcopy(rooms)
      case1_3 = up(y, x, case1_3)
      install(n + 1, k, case1_3)
      case1_4 = deepcopy(rooms)
      case1_4 = down(y, x, case1_4)
      install(n + 1, k, case1_4)

    elif num == 2: # 2번 cctv 인 경우 총 2가지 경우가 존재
      case2_1 = deepcopy(rooms)
      case2_1 = left(y, x, case2_1)
      case2_1 = right(y, x, case2_1)
      install(n + 1, k, case2_1)
      case2_2 = deepcopy(rooms)
      case2_2 = up(y, x, case2_2)
      case2_2 = down(y, x, case2_2)
      install(n + 1, k, case2_2)

    elif num == 3: # 3번 cctv 인 경우 총 4가지 경우가 존재
      case3_1 = deepcopy(rooms)
      case3_1 = left(y, x, case3_1)
      case3_1 = up(y, x, case3_1)
      install(n + 1, k, case3_1)
      case3_2 = deepcopy(rooms)
      case3_2 = right(y, x, case3_2)
      case3_2 = up(y, x, case3_2)
      install(n + 1, k, case3_2)
      case3_3 = deepcopy(rooms)
      case3_3 = left(y, x, case3_3)
      case3_3 = down(y, x, case3_3)
      install(n + 1, k, case3_3)
      case3_4 = deepcopy(rooms)
      case3_4 = right(y, x, case3_4)
      case3_4 = down(y, x, case3_4)
      install(n + 1, k, case3_4)

    elif num == 4: # 4번 cctv 인 경우 4가지 경우가 존재
      case4_1 = deepcopy(rooms)
      case4_1 = left(y, x, case4_1)
      case4_1 = right(y, x, case4_1)
      case4_1 = up(y, x, case4_1)
      install(n + 1, k, case4_1)
      case4_2 = deepcopy(rooms)
      case4_2 = right(y, x, case4_2)
      case4_2 = up(y, x, case4_2)
      case4_2 = down(y, x, case4_2)
      install(n + 1, k, case4_2)
      case4_3 = deepcopy(rooms)
      case4_3 = left(y, x, case4_3)
      case4_3 = up(y, x, case4_3)
      case4_3 = down(y, x, case4_3)
      install(n + 1, k, case4_3)
      case4_4 = deepcopy(rooms)
      case4_4 = right(y, x, case4_4)
      case4_4 = down(y, x, case4_4)
      case4_4 = left(y, x, case4_4)
      install(n + 1, k, case4_4)

    else: # 5번 cctv 인 경우 1가지 경우가 존재
      case5 = deepcopy(rooms)
      case5 = left(y, x, case5)
      case5 = right(y, x, case5)
      case5 = up(y, x, case5)
      case5 = down(y, x, case5)
      install(n + 1, k, case5)


Y, X = map(int, input().split())
cctv_cnt = 0 # cctv 개수
cctv_list = [] # cctv 번호, 위치를 저장할 리스트
cctv_num = [1, 2, 3, 4, 5]
min_value = Y * X
room_info = [list(map(int, input().split())) for _ in range(Y)]
for i in range(Y):
  for j in range(X):
    if room_info[i][j] in cctv_num:
      cctv_list.append([room_info[i][j], i, j])
      cctv_cnt += 1
install(0, cctv_cnt, room_info)
print(min_value)