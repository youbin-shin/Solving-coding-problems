N, K = map(int, input().split())
container = list(map(int, input().split())) # 컨테이너의 내구도를 저장할 리스트
for i in range(2 * N):
    container[i] = [container[i], 0]
# container[i] = [i칸의 내구도, 로봇유무] => 로봇이 있으면 -1, 없으면 0

step = 0 # 출력할 변수, 몇 단계 진행중인지 카운트할 변수
up = 0 # 올라가는 위치 인덱스
down = N - 1 # 내려가는 위치 인덱스

while True:
    step += 1
    # 1. 벨트가 한칸 회전한다.
    up -= 1
    if up < 0: up = 2 * N - 1
    if container[down][1] == -1: # 로봇이 있는 경우 내리기
        container[down][1] = 0
    down -= 1
    if down < 0: down = 2 * N - 1

    # 2. 로봇을 이동한다.
    move = down
    for _ in range(N):
        if container[move][1] == -1: # 로봇이 있는 경우
            if move == down: # 내리는 위치이기에 로봇은 땅으로 내려가는 경우
                container[move][1] = 0
            else:
                # 로봇이 옆 칸으로 이동하는 경우
                next_move = move + 1
                if next_move == 2 * N: next_move = 0
                # 이동할 옆 칸에 로봇이 없고 내구도가 1 이상인 경우 이동하기
                if container[next_move][1] == 0 and container[next_move][0] != 0:
                    container[move][1] = 0
                    container[next_move][0] -= 1
                    container[next_move][1] = -1
        move -= 1
        if move < 0: move = 2 * N - 1

    # 3. 가능하다면 로봇을 올린다.
    if container[up][1] == 0 and container[up][0] != 0:
        container[up][0] -= 1
        container[up][1] = -1 # 로봇 있음 체크

    cnt = 0
    for n in range(2 * N):
        if container[n][0] == 0: # 내구도가 0인 칸 세기
            cnt += 1
    if cnt >= K:
        break

print(step)
