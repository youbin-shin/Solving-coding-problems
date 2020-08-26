import copy

def pull(m, n, board): # 블록이 지워진 뒤 아래로 당기는 함수
    for j in range(n):
        temp = []
        for i in range(m):
            if board[i][j]:
                temp.append(board[i][j])
        for i2 in range(m-1, -1, -1):
            if temp:
                board[i2][j] = temp.pop()
            else:
                board[i2][j] = 0
    return board


def bomb(m, n, board): # 2X2 같은 블록을 보면 지우는 함수
    next_board = copy.deepcopy(board)

    for i in range(m):
        for j in range(n):
            if i < m - 1 and j < n - 1 and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                dirs = [[0, 0], [1, 0], [0, 1], [1, 1]]
                for d in range(4):
                    new_i = i + dirs[d][0]
                    new_j = j + dirs[d][1]
                    if board[i][j] == next_board[new_i][new_j]:
                        next_board[new_i][new_j] = 0

    ans = 0
    if board != next_board: # 변화가 있다면 밑으로 댕기고 다시 확인하자.
        next_board = pull(m, n, next_board)
        return bomb(m, n, next_board)
    else:
        for l in range(len(board)): 
            ans += board[l].count(0) # 0을 카운트 즉, 사라진 블록의 개수 구하기
        return ans


def solution(m, n, board):
    for i in range(len(board)):
        board[i] = list(board[i])
    answer = bomb(m, n, board)
    return answer


# m = 4
# n = 5
# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# print(solution(m, n, board))