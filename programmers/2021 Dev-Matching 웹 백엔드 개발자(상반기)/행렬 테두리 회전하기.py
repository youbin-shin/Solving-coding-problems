board = []
def solution(rows, columns, queries):
    global board
    answer = []
    # 1. 초기 그림 만들기
    board = [[0] * columns for _ in range(rows)]
    i = 1
    for r in range(rows):
        for c in range(columns):
            board[r][c] = i
            i += 1

    def rotate(y1, x1, y2, x2): # 2. 회전하며 이동한 최소 숫자 출력하기
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        d = 0
        temp = board[y1][x1]
        my, mx = y1, x1
        min_value = temp
        while True:
            nmy, nmx = my + dirs[d][0], mx + dirs[d][1]
            if d == 3 and [nmy, nmx] == [y1, x1]:
                board[my][mx] = temp
                break
            min_value = min(min_value, board[nmy][nmx])
            board[my][mx] = board[nmy][nmx]
            if nmy in (y1, y2) and nmx in (x1, x2):
                d += 1
            my, mx = nmy, nmx
        return min_value

    for q in queries:
        answer.append(rotate(q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1))
    return answer