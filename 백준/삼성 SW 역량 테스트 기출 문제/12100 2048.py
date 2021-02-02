from itertools import product # 중복 순열
from copy import deepcopy

def rightBlock(t_board):
    # 같은 수를 만나면 2 곱해주기
    for r in range(N):
        if sum(t_board[r]) != 0:
            for c in range(N - 1, 0, -1):
                if t_board[r][c] != 0:
                    num1 = t_board[r][c]
                    change_idx = 0
                    num2 = -1
                    for c2 in range(c - 1, -1, -1):
                        if t_board[r][c2] != 0:
                            num2 = t_board[r][c2]
                            change_idx = c2
                            break
                    if num2 == num1: # 같은 수인 경우
                        t_board[r][c] *= 2
                        t_board[r][change_idx] = 0
    # 숫자 사이에 0이 없도록 땡기기
    for r in range(N):
        if sum(t_board[r]) != 0:
            for c in range(N - 1, -1, -1):
                if t_board[r][c] == 0: # 행에 존재하는 0을 지우기
                    t_board[r].pop(c)
            while len(t_board[r]) < N: # 지워진 0만큼 행 앞에 추가하기
                t_board[r].insert(0, 0)


def leftBlock(t_board):
    # 같은 수를 만나면 2 곱해주기
    for r in range(N):
        if sum(t_board[r]) != 0:
            for c in range(N - 1):
                if t_board[r][c] != 0:
                    num1 = t_board[r][c]
                    change_idx = 0
                    num2 = -1
                    for c2 in range(c + 1, N):
                        if t_board[r][c2] != 0:
                            num2 = t_board[r][c2]
                            change_idx = c2
                            break
                    if num2 == num1: # 같은 수인 경우
                        t_board[r][c] *= 2
                        t_board[r][change_idx] = 0
    # 숫자 사이에 0이 없도록 땡기기
    for r in range(N):
        if sum(t_board[r]) != 0:
            for c in range(N - 1, -1, -1): # 행에 존재하는 0을 지우기
                if t_board[r][c] == 0:
                    t_board[r].pop(c)
            while len(t_board[r]) < N: # 지워진 0을 뒤에 추가하기
                t_board[r].append(0)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_block = 0 # 가장 큰 블록을 저장할 변수, 출력할 값
# move_ways : 4가지 방향(위, 아래, 왼쪽, 오른쪽)에 대한 모든 5번 이동하는 모든 경우의 수를 저장한 리스트 (중복 순열 이용)
move_ways = list(product(range(4), repeat=5))

for m_list in move_ways: # 완전 탐색
    test_board = deepcopy(board) # 5번의 이동을 저장할 리스트
    for m in m_list:
        if m == 0: # 왼쪽으로 미는 경우
            leftBlock(test_board)

        elif m == 1: # 오른쪽으로 미는 경우
            rightBlock(test_board)

        elif m == 2: # 위로 미는 경우 (시계방향으로 90도 회전시키고 오른쪽으로 밀기)
            turn_board = [[0] * N for _ in range(N)]
            # 1. 시계방향으로 90도 회전시키기
            for r in range(N):
                for c in range(N):
                    turn_board[c][N - 1 - r] = test_board[r][c]
            # 2. 오른쪽으로 밀기
            rightBlock(turn_board)
            # 시계 방향으로 회전시킨 것을 270도 회전하여 원상태로 만들기
            for r2 in range(N):
                for c2 in range(N):
                    test_board[N - 1 - c2][r2] = turn_board[r2][c2]

        else: # 아래로 미는 경우 (시계방향으로 90도 회전시키고 왼쪽으로 밀기)
            turn_board = [[0] * N for _ in range(N)]
            # 1. 시계방향으로 90도 회전시키기
            for r in range(N):
                for c in range(N):
                    turn_board[c][N - 1 - r] = test_board[r][c]
            # 2. 오른쪽으로 밀기
            leftBlock(turn_board)
            # 시계 방향으로 회전시킨 것을 270도 회전하여 원상태로 만들기
            for r2 in range(N):
                for c2 in range(N):
                    test_board[N - 1 - c2][r2] = turn_board[r2][c2]

    # 가장 큰 블록이 있는지 탐색하기
    for n in range(N):
        max_block = max(max_block, max(test_board[n]))

print(max_block)
