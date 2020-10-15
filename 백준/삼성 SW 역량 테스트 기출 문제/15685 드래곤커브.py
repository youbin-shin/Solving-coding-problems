board = [[0] * 101 for _ in range(101)] 
dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]

for _ in range(int(input())):
  x, y, d, g = map(int, input().split())
  end_y, end_x = y, x # 가장 끝 점을 저장할 변수
  temp = [[y, x]] # 드래곤 커브를 저장할 리스트
  d_list = [d] # 이동 방향을 저장할 리스트
  # 0세대 만들기
  end_y, end_x = end_y + dirs[d][0], end_x + dirs[d][1]
  temp.append([end_y, end_x])

  for _ in range(g): # 1세대 부터 g 까지
    d_temp = []
    for d in range(len(d_list)): # 끝 점을 기준으로 최근으로 저장한 방향을 통해 움직일 방향 찾아 움직이기
      m_d = (d_list[d] + 1) % 4 # 움직여야할 방향
      end_y, end_x = end_y + dirs[m_d][0], end_x + dirs[m_d][1]
      temp.append([end_y, end_x])
      d_temp.append(m_d)
    d_list = d_temp[::-1] + d_list
  for t in range(len(temp)): # 드래곤 커브의 정보 저장
    board[temp[t][0]][temp[t][1]]  += 1

cnt = 0
# 네 곳 모두 드래곤 커브의 일부분인지 확인하는 단계
for y in range(100):
  for x in range(100):
    if board[y][x] != 0 and board[y][x + 1] != 0 and board[y + 1][x] != 0 and board[y + 1][x + 1] != 0:
      cnt += 1

print(cnt)