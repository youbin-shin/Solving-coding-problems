# Sol1 : DP
# 정사각형이 되는 조건 : 위의 값, 대각선의 값, 옆의 값이 1일 경우
def solution(board):
    X = len(board[0])
    Y = len(board)
    for x in range(1, X):
        for y in range(1, Y):
            if board[y][x]:
                # 기준 좌표로 부터 위, 좌측상단 대각선, 좌측 옆 살피기
                board[y][x] = min(board[y - 1][x], board[y - 1][x - 1], board[y][x - 1]) + 1
    answer = max([b for row in board for b in row])
    return answer * answer


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[1, 0], [0, 0]]
print(solution(board))


# Sol2 : 완전 탐색 방법 (효율성에서 시간 초과 발생)
# def solution(board):
#     answer = 0
#     X = len(board[0])
#     Y = len(board)
#     N = min(X, Y)
#     for n in range(N, 0, -1): # 가장 큰 정사각형이 가능한 경우부터 탐색
#         if answer != 0: break
#         # 탐색할 시작 좌표 x, y 범위 정하기
#         for x in range(X - n + 1):
#             if answer != 0: break
#             for y in range(Y- n + 1):
#                 if answer != 0: break
#                 frag = False
#                 # n의 범위(가로 d2, 세로 d) 탐색하는 반복문
#                 for d in range(n):
#                     if frag or answer!= 0: break
#                     for d2 in range(n):
#                         if board[y + d2][x + d] == 0:
#                             frag = True
#                             break
#                 if frag == False:
#                     answer = n
#     return answer * answer
