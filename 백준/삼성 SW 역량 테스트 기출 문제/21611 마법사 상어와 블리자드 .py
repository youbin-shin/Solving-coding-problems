# 63%에서 실패된다면 구슬이 아무것도 없는 경우에 대한 indexError이다. -> 디버깅시 극단적 상황에 대한 테스트 케이스로 확인하기

def find_ball_list(board):
    global mid_y, mid_x
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    y, x = mid_y, mid_x
    d = 0
    move_cnt = 1
    change_move_cnt = 0
    ball_list = []
    flug = False
    while True:
        if flug:
            break
        for _ in range(move_cnt):
            y, x = y + dirs[d][0], x + dirs[d][1]
            if [y, x] == [0, 0]:
                flug = True
                break
            if board[y][x] != 0:
                ball_list.append(board[y][x])
        d = (d + 1) % 4
        change_move_cnt += 1
        if change_move_cnt == 2:
            move_cnt += 1
            change_move_cnt = 0
    return ball_list


def update_board_numbers(board_numbers):
    global mid_y, mid_x, N

    next_board = [[0] * N for _ in range(N)]
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    y, x = mid_y, mid_x
    d = 0
    move_cnt = 1
    change_move_cnt = 0
    idx = 0
    flug = False

    while True:
        if flug:
            break
        for _ in range(move_cnt):
            if [y, x] == [0, 0]:
                flug = True
                break
            y, x = y + dirs[d][0], x + dirs[d][1]

            next_board[y][x] = board_numbers[idx]
            idx += 1
            if idx == len(board_numbers):
                flug = True
                break
        d = (d + 1) % 4
        change_move_cnt += 1
        if change_move_cnt == 2:
            move_cnt += 1
            change_move_cnt = 0
    return next_board


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
M_list = [list(map(int, input().split())) for _ in range(M)]
mid_y, mid_x = N // 2, N // 2

burned_ball = [0] * 4


m_dirs = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]] # 블리자드 마법 방향
for d, s in M_list:
    # 1. 블리자드 마법 실행하여 구슬 파괴
    y, x = mid_y, mid_x
    for _ in range(s):
        y, x = y + m_dirs[d][0], x + m_dirs[d][1]
        if 0 <= y < N and 0 <= x < N:
            board[y][x] = 0
        
    # 2. 구슬 이동
    ball_list = find_ball_list(board)

    # 3. 구슬 폭발 (4개 이상 연속 구슬인 경우)
    # 폭발 전과 후가 같아질 때까지 실행
    while ball_list:
        next_ball_list = []
        ball_num = ball_list[0]
        ball_cnt = 0
        for b in range(len(ball_list) + 1):
            if b < len(ball_list) and ball_num == ball_list[b]:
                ball_cnt += 1
            else:
                if ball_cnt >= 4: # 구슬 폭발
                    burned_ball[ball_num] += ball_cnt
                else:
                    next_ball_list.extend([ball_num] * ball_cnt)
                if b == len(ball_list):
                    break
                ball_num = ball_list[b]
                ball_cnt = 1

        if ball_list == next_ball_list:
            break
        ball_list = next_ball_list

    # 보드 새로 채우기
    board_numbers = []
    if ball_list:
        ball_num = ball_list[0]
        ball_cnt = 0
        for ball in ball_list:
            if ball_num == ball:
                ball_cnt += 1
            else:
                board_numbers.extend([ball_cnt, ball_num])
                ball_num = ball
                ball_cnt = 1
        board_numbers.extend([ball_cnt, ball_num])
        board = update_board_numbers(board_numbers)

answer = 0
for i in range(1, 4):
    answer += burned_ball[i] * i
print(answer)