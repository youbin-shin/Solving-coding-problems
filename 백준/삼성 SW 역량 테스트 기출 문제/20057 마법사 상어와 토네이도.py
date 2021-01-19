N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
y, x, d = N // 2, N // 2, 0 # 시작좌표와 방향 설정

dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
tornado_dirs = [ # 토네이도로 흩날릴 방향 저장
    [[-2, 0], [2, 0], [-1, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [1, -1], [0, -2], [0, -1]],
    [[0, -2], [0, 2], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 1], [2, 0], [1, 0]], # 바꾸고 앞인데긋에 -1 곱하면 똑디
    [[2, 0], [-2, 0], [1, -1], [-1, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [0, 2], [0, 1]],
    [[0, 2], [0, -2], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, -1], [-2, 0], [-1, 0]]
]
move_cnt = [1, 0] # 움직이는 방향 바꾸는 기준이 될 리스트

frag = False # 종료 조건의 기준
answer = 0 # 격자 밖으로 나간 모래의 양 저장할 변수
while True:
    if frag: break # 종료조건
    for _ in range(move_cnt[0]): # 한방향으로 이동하는 횟수
        y += dirs[d][0]
        x += dirs[d][1]
        if [y, x] == [0, 0]: # 최종 이동이기에 frag = True로 바꾸기
            frag = True

        # 모래 흩날리는 과정
        sand = board[y][x] # y 칸의 모래양 저장
        board[y][x] = 0
        temp_sand = 0 # 남은 모래 알파의 값을 저장할 변수
        for t in range(4):
            tornado = [0.02, 0.01, 0.07, 0.1]
            for t2 in range(2):
                temp_sand += int(sand * tornado[t])
                ty, tx = y + tornado_dirs[d][2 * t + t2][0], x + tornado_dirs[d][2 * t + t2][1]
                if 0 <= ty < N and 0 <= tx < N:
                    board[ty][tx] += int(sand * tornado[t])
                else: # 격자 밖으로 나간 모래의 양
                    answer += int(sand * tornado[t])
        ty, tx = y + tornado_dirs[d][8][0], x + tornado_dirs[d][8][1]
        temp_sand += int(sand * 0.05)
        if 0 <= ty < N and 0 <= tx < N:
            board[ty][tx] += int(sand * 0.05)
        else:  # 격자 밖으로 나간 모래의 양
            answer += int(sand * 0.05)
        ly, lx = y + tornado_dirs[d][9][0], x + tornado_dirs[d][9][1]
        if 0 <= ly < N and 0 <= lx < N:
            board[ly][lx] += sand - temp_sand
        else:  # 격자 밖으로 나간 모래의 양
            answer += sand - temp_sand

    # 토네이도의 이동, 방향 결정
    d += 1
    if d == 4: d = 0
    move_cnt[1] += 1
    if move_cnt[1] == 2: # 움직이는 방향 바꾸기
        move_cnt[0] += 1
        move_cnt[1] = 0

print(answer)