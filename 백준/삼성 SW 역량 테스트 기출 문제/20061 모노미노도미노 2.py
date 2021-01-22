def checkBlock(color): # 4행 칸이 모두 타일로 찾는지 확인하는 함수
    global score
    if color == "green":
        board = green_board
    else:
        board = blue_board
    idx = 5
    while idx >= 0:
        if sum(board[idx]) == 4: # 칸이 다 차있을 때 지우고 이동하기
            board.pop(idx)
            board.insert(0, [0] * 4)
            score += 1
        else:
            idx -= 1


def greenBlock(t, x): # 초록색 판에서 일어나는 과정 함수
    # 1. 초록색 판에 블록 넣기
    if t == 1: # 블록이 1번 타입인 경우
        for g in range(1, 6):
            if green_board[g][x] != 0:
                green_board[g - 1][x] = 1
                break
            if g == 5:
                # 다른 블록을 만난 적없기에 끝에 위치하기
                green_board[g][x] = 1
    elif t == 2: # 블록이 2번 타입인 경우
        for g in range(1, 6):
            if green_board[g][x] != 0 or green_board[g][x + 1] != 0:
                green_board[g - 1][x] = 1
                green_board[g - 1][x + 1] = 1
                break
            if g == 5:
                green_board[g][x] = 1
                green_board[g][x + 1] = 1
    else: # t == 3 | 블록이 1번 타입인 경우
        for g in range(1, 5):
            if green_board[g][x] != 0 or green_board[g + 1][x] != 0:
                green_board[g - 1][x] = 1
                green_board[g][x] = 1
                break
            if g == 4:
                green_board[g][x] = 1
                green_board[g + 1][x] = 1

    # 2. 각 행별 모든 칸이 차있는지 확인하기
    checkBlock("green")

    # 3. 특별한 칸(연한색) 확인하기
    if sum(green_board[0]) != 0:
            green_board.pop()
            green_board.insert(0, [0] * 4)
    if sum(green_board[1]) != 0:
        green_board.pop()
        green_board.insert(0, [0] * 4)


def blueBlock(t, y): # 파란색 판에서 일어나는 과정 함수
    # 1. 파란색 판에 블록 넣기
    if t == 1:
        for b in range(1, 6):
            if blue_board[b][y] != 0:
                blue_board[b - 1][y] = 1
                break
            if b == 5:
                blue_board[b][y] = 1
    elif t == 2:
        for b in range(1, 5):
            if blue_board[b][y] != 0 or blue_board[b + 1][y] != 0:
                blue_board[b - 1][y] = 1
                blue_board[b][y] = 1
                break
            if b == 4:
                blue_board[b][y] = 1
                blue_board[b + 1][y] = 1
    else:  # t == 3 | 블록이 1번 타입인 경우
        for b in range(1, 6):
            if blue_board[b][y] != 0 or blue_board[b][y + 1] != 0:
                blue_board[b - 1][y] = 1
                blue_board[b - 1][y + 1] = 1
                break
            if b == 5:
                blue_board[b][y] = 1
                blue_board[b][y + 1] = 1

    # 2. 각 행별 모든 칸이 차있는지 확인하기
    checkBlock("blue")

    # 3. 특별한 칸(연한색) 확인하기
    if sum(blue_board[0]) != 0:
        blue_board.pop()
        blue_board.insert(0, [0] * 4)
    if sum(blue_board[1]) != 0:
        blue_board.pop()
        blue_board.insert(0, [0] * 4)


green_board = [[0] * 4 for _ in range(6)] # 초록색 보드
blue_board = [[0] * 4 for _ in range(6)] # 파란색 보드
score = 0 # 행이 사라져 점수가 획득을 저장할 변수

N = int(input())
for _ in range(N):
    t, y, x = list(map(int, input().split())) # 블록 입력받기
    greenBlock(t, x)
    blueBlock(t, y)

# 최종적으로 결과값 출력하기
print(score)
left_block = 0
for b in range(6):
    left_block += sum(green_board[b])
    left_block += sum(blue_board[b])
print(left_block)