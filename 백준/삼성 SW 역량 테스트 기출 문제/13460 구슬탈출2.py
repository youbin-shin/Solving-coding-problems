from collections import deque

def pullBall(y, x, d): # 방향 d로 기울였을 때 굴러가는 최종 위치 찾아주는 함수
    move_cnt = 0 # 얼마나 움직였는지 체크해주는 변수
    ny, nx = y, x
    while True:
        ny, nx = ny + dirs[d][0], nx + dirs[d][1]
        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == ".": # 빈칸이기에 이동하기
                move_cnt += 1
                y, x = ny, nx
            elif board[ny][nx] == "O":
                move_cnt = -1 # 목적지에 도착했다는 것을 -1로 저장
                return ny, nx, move_cnt
            else:
                break
        else:
            break
    return y, x , move_cnt


def moveBall(first_red_y, first_red_x, first_blue_y, first_blue_x): # 구슬을 굴려서 최종 O에 가는 곳을 구해주는 함수
    global answer
    q = deque()
    visited = []
    q.append([first_red_y, first_red_x, first_blue_y, first_blue_x, 0])
    visited.append([first_red_y, first_red_x, first_blue_y, first_blue_x])
    while q: # BFS 를 통해 이동 시키기
        red_y, red_x, blue_y, blue_x, cnt = q.popleft()
        for d in range(4):
            # 각 방향별로 pullBall 함수를 통해 굴러간 마지막 위치 찾기
            next_red_y, next_red_x, red_cnt = pullBall(red_y, red_x, d)
            next_blue_y, next_blue_x, blue_cnt = pullBall(blue_y, blue_x, d)

            if [next_red_y, next_red_x, next_blue_y, next_blue_x] != [red_y, red_x, blue_y, blue_x]: # 움직임의 변화가 있었을 때만 확인하기(가지치기)
                if [next_red_y, next_red_x, next_blue_y, next_blue_x] not in visited: # 이동안했던 곳일 경우로 체크!
                    if blue_cnt == -1: # 파란구슬이 구멍에 들어간 경우이기에 해당 경우 continue를 통해 확인하지 말기
                        continue
                    if red_cnt == -1 and cnt + 1 <= 10: # 빨간구슬이 구멍에 들어간 경우 "종료 조건"
                        answer = cnt + 1
                        return
                    if [next_red_y, next_red_x] == [next_blue_y, next_blue_x]: # 같은 위치인 경우
                        if red_cnt > blue_cnt: # 빨간구슬이 더 많이 움직임 => 파란구슬 뒤에 있기에 빨간구슬을 후퇴시키기!
                            next_red_y, next_red_x = next_red_y - dirs[d][0], next_red_x - dirs[d][1]
                        else: # 파란구슬이 더 많이 움직임 => 빨간구슬 뒤에 있기에 파란구슬을 후퇴시키기!
                            next_blue_y, next_blue_x = next_blue_y - dirs[d][0], next_blue_x - dirs[d][1]
                    if cnt + 1 <= 10: # 10번 이하로 움직인 경우만 확인하면 되기에!
                        q.append([next_red_y, next_red_x, next_blue_y, next_blue_x, cnt + 1])
                        visited.append([next_red_y, next_red_x, next_blue_y, next_blue_x])


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
answer = - 1
first_red_y = -1
first_red_x = -1
first_blue_y = -1
first_blue_x = -1

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 방향: 0-상 1-우 2-하 3-좌
for n in range(N):
    for m in range(M):
        # 구슬 위치 저장 후 움직일 수 있도록 빈칸으로 바꾸기
        if board[n][m] == "R":
            first_red_y, first_red_x = n, m
            board[n][m] = "."
        if board[n][m] == "B":
            first_blue_y, first_blue_x = n, m
            board[n][m] = "."

moveBall(first_red_y, first_red_x, first_blue_y, first_blue_x) # 구슬을 굴려서 최종 O에 가는 곳을 구해주는 함수

print(answer)