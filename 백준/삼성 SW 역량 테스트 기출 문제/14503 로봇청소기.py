import sys
sys.setrecursionlimit(100000)

def search(y, x, d, rotate):
    ly = y + left_dirs[d][0]
    lx = x + left_dirs[d][1]
    if room[ly][lx] == 0: # (문제에서 로봇청소기 작동 2번 a)
        clean(ly, lx, left_dirs[d][2])
    else:
       if rotate == 4: # 네방향 모두 청소가 이미 되어있거나 벽인 경우
            by = y + back_dirs[d][0]
            bx = x + back_dirs[d][1]
            if room[by][bx] == 1: # (문제에서 로봇청소기 작동 2번 d)
                return
            else: # (문제에서 로봇청소기 작동 2번 c)
                search(by, bx, d, 0)
       else: # (문제에서 로봇청소기 작동 2번 b)
           search(y, x, left_dirs[d][2], rotate + 1)

def clean(y, x, d): # 청소하는 함수 (문제에서 로봇청소기 작동 1번)
    global cnt
    cnt += 1
    visited[y][x] = 1
    room[y][x] = 2
    search(y, x, d, 0) # 탐색하는 함수 (문제에서 로봇청소기 작동 2번)

# 입력받기
Y, X = map(int, input().split())
y, x, d = map(int, input().split()) # 로봇청소기 위치와 방향 저장
room = [list(map(int, input().split())) for _ in range(Y)]

# 방향
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북 동 남 서
left_dirs = [[0, -1, 3], [-1, 0, 0], [0, 1, 1], [1, 0, 2]] # dirs 인덱스 기준 왼쪽 방향과 dirs의 왼쪽 방향 인덱스 저장
back_dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]] # dirs 인덱스 기준 후진 방향
visited = [[0]*X for _ in range(Y)] # 청소했는지를 확인하는 리스트
cnt = 0 # 청소한 칸의 개수 저장할 변수
clean(y, x, d) # 현재 위치는 항상 빈칸 즉 청소하기 위한 함수 호출
print(cnt)