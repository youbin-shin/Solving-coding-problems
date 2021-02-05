def roadCheck(road): # 길이 가능한지 탐색하는 함수
    global answer, L
    add = [] # 경사로를 추가할 위치를 저장할 리스트
    if len(road) == 1: # 길이 가능한 경우
        answer += 1
        return
    else:
        idx = -1
        for r in range(len(road) - 1):
            idx += road[r][1]
            # 낮은 칸과 높은 칸 차이가 1인 경우
            if road[r][0] - road[r + 1][0] == 1:
                if road[r + 1][1] >= L: # 낮은 칸에 L개의 경사로 놓을 수 있는 경우
                    for i in range(idx + 1, idx + 1 + L):
                        if i in add: # 경사로를 놓은 곳에 경사로를 놓는 경우 => 길 불가능
                            return
                        else:
                            add.append(i)
                else:
                    return
            # 낮은 칸과 높은 칸 차이가 1인 경우
            elif road[r][0] - road[r + 1][0] == -1:
                if road[r][1] >= L: # 낮은 칸에 L개의 경사로 놓을 수 있는 경우
                    for i in range(idx, idx - L, -1):
                        if i in add: # 경사로를 놓은 곳에 경사로를 놓는 경우 => 길 불가능
                            return
                        else:
                            add.append(i)
                else:
                    return
            else: # 길이 될 수 없는 경우
                return
        answer += 1


def rowCheck(N): # 행에 대한 정보를 저장하는 함수
    # 각 행에 대해서 연속된 수(num)가 몇개(cnt)인지 정보를 저장한다.
    for r in range(N):
        cnt = 0 # 연속된 숫자의 개수를 세는 변수
        num = -1 # board의 숫자를 저장하는 변수
        row = [] # [num, cnt]에 대한 각 행의 정보를 저장할 이중 리스트
        for c in range(N):
            if num == -1:
                num = board[r][c]
                cnt = 1
            elif num == board[r][c]: # 같은 수인 경우(연속된 같은 수)
                cnt += 1
            else: # 다른 수인 경우
                row.append([num, cnt])
                num = board[r][c]
                cnt = 1
        if num != -1:
            row.append([num, cnt])
        roadCheck(row) # 길이 가능한지 탐색하는 함수


def colCheck(N): # 열에 대한 정보를 저장하는 함수
    # 각 열에 대해서 연속된 수(num)가 몇개(cnt)인지 정보를 저장한다.
    for c in range(N):
        cnt = 0  # 연속된 숫자의 개수를 세는 변수
        num = -1  # board의 숫자를 저장하는 변수
        col = [] # [num, cnt]에 대한 각 행의 정보를 저장할 이중 리스트
        for r in range(N):
            if num == -1:
                num = board[r][c]
                cnt = 1
            elif num == board[r][c]: # 같은 수인 경우(연속된 같은 수)
                cnt += 1
            else: # 다른 수인 경우
                col.append([num, cnt])
                num = board[r][c]
                cnt = 1
        if num != -1:
            col.append([num, cnt])
        roadCheck(col) # 길이 가능한지 탐색하는 함수


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
# 행에서 가능한 길 찾기
rowCheck(N)
# 열에서 가능한 길 찾기
colCheck(N)

print(answer)