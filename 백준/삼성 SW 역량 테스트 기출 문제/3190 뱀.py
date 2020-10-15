N = int(input())
board = [[0]*N for _ in range(N)]
snake_info = []
y, x, d = 0, 0, 0 # 뱀이 머리 위치 좌표와 방향 저장할 변수
snake_list = [[0, 0]] # 뱀이 어디에 있는지 좌표를 저장할 리스트
dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
info = 0 
time = 0

# 사과 위치 저장하기
for _ in range(int(input())):
  i, j = map(int, input().split())
  board[i-1][j-1] = 1
# 뱀의 방향 정보 저장하기
for _ in range(int(input())):
  X, C = map(str, input().split())
  snake_info.append([int(X), C])

while True:
  time += 1
  y, x = y + dirs[d][0], x + dirs[d][1]
  # 종료조건
  if [y, x] in snake_list: break # 뱀이 자기자신과 만날 경우
  if y < 0 or x < 0 or y >= N or x >= N: # 벽에서 벗어난 경우
    break

  if board[y][x]== 1: # 사과일 경우
    board[y][x] = 0 
  else:
    snake_list.pop(0) # 사과가 없기에 뱀의 꼬리 부분이 이동하여 빼주기

  snake_list.append([y, x]) # 뱀의 머리 부분 저장

  if info < len(snake_info) and time == snake_info[info][0]:
    if snake_info[info][1] == "L": # 왼쪽으로 방향을 돌리기
      d = (d + 1) % 4
    else:
      d = (d + 3) % 4
    info += 1

print(time)