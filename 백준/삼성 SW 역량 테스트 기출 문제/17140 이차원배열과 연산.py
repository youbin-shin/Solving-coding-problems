r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
time = 0

while True:
  if time > 100: # 시간이 100초 초과할 조건
    time = -1
    break
  if len(A) >= r and len(A[0]) >= c and A[r-1][c-1] == k: # 종료조건
    break
  time += 1
  R_len = len(A)
  C_len = len(A[0])
  length = 0 # 행이나 열중에서 가장 긴 길이를 저장하는 변수

  # 행연산
  if R_len >= C_len:
    R_list = []
    temp_list = []
    for y in range(R_len):
      num = [] # [숫자, 숫자의 빈도수] 저장할 리스트
      for i in range(len(A[y])):
        frag = True
        if A[y][i] != 0: # 0은 카운트하지 않는 조건
          for n in range(len(num)):
            if A[y][i] == num[n][0]:
              num[n][1] += 1
              frag = False
          if frag:
            num.append([A[y][i], 1])
            
      num = sorted(num, key=lambda x: (x[1], x[0])) # 빈도수 오름차순 기준, 수 오름차순 기준 정렬
      temp_list.append(num)
      if length < len(num) * 2:
        length = len(num) * 2 # 가장 긴 길이를 저장
    if length > 100:
      length = 100
    for j in range(len(temp_list)):
      temp = []
      for z in range(len(temp_list[j])):
        temp += temp_list[j][z] 
      if len(temp) > 100: # 길이가 100 넘을 경우 100까지 자르기
        A[j] = temp[j][:100]
      else: # 가장 긴 길이 기준으로 0 채워주기
        diff = length - len(temp)
        A[j] = temp + [0] * diff

  # 열연산
  else:
    C_list = []
    temp_list = []
    for x in range(C_len):
      num = []
      col_temp = []
      for y in range(R_len):
        col_temp.append(A[y][x])
      for i in range(len(col_temp)):
        if col_temp[i] != 0:
          frag = True
          for n in range(len(num)):
            if col_temp[i] == num[n][0]:
              num[n][1] += 1
              frag = False
          if frag:
            num.append([col_temp[i], 1])
      num = sorted(num, key=lambda x: (x[1], x[0])) # 빈도수 오름차순 기준, 수 오름차순 기준 정렬
      if length < len(num) * 2:
        length = len(num) * 2 # 가장 긴 길이를 저장
      temp_list.append(num)
    if length > 100:
      length = 100

    for j in range(len(temp_list)):
      temp = []
      for z in range(len(temp_list[j])):
        temp += temp_list[j][z]

      if len(temp) > 100: # 길이가 100 넘을 경우 100까지 자르기
        C_list.append(temp[j][:100])
      else: # 가장 긴 길이 기준으로 0 채워주기
        diff = length - len(temp)
        C_list.append(temp + [0] * diff)

    A = []
    # 행으로 저장되있는 C_list를 열로 바꿔주는 과정
    for ny in range(len(C_list[0])):
      A_ready = []
      for nx in range(len(C_list)):
        A_ready.append(C_list[nx][ny])
      A.append(A_ready)


print(time)