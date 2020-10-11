def pick(g, r, visited): # 톱니바퀴 회전을 통해 변화가 필요한 것 구하는 함수
    visited[g] = 1
    front_g, back_g = g - 1, g + 1 # 앞 뒤로 확인 필요
    change_list.append([g, r])
    if front_g >= 0 and visited[front_g]==0: # 앞 톱니바퀴와 변화가 필요한지 확인
      if gear[front_g][2] != gear[g][6]:
         visited[front_g] = 1
         pick(front_g, r * (-1), visited)
    if back_g < 4 and visited[back_g] == 0: # 뒷 톱니바퀴와 변화가 필요한지 확인
      if gear[back_g][6] != gear[g][2]:
         visited[back_g] = 1
         pick(back_g, r * (-1), visited)


# 입력받기
gear = [list(map(int, input())) for _ in range(4)]
rotate_num = int(input())
rotate = [list(map(int, input().split())) for _ in range(rotate_num)]

for i in range(rotate_num):
   change_list = [] # 회전을 통해 변화가 필요한 톱니바퀴번호와 회전방향 저장할 리스트
   pick(rotate[i][0]-1, rotate[i][1], [0, 0, 0, 0]) # 회전을 통해 변해야할 톱니 계산하는 함수
   for j in change_list:
        temp = gear[j[0]]
        if j[1] == 1: # 시계방향 회전
            temp.insert(0, temp.pop())
            gear[j[0]] = temp
        else: # 반시계방향 회전
            temp.append(temp.pop(0))
            gear[j[0]] = temp
answer = 0
for i in range(4):
   answer += gear[i][0] * (2 ** i)
print(answer)