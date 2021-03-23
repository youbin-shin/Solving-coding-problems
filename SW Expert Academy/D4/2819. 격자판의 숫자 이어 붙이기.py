def move(k, x, y, result, num): # k는 자릿수, num은 만들어지는 수
    if k == 7: # 7자리 수가 되면
        if num not in result: # result 리스트에 값이 없으면
            result.append(num) # 추가한 다음에
        return # 끝낸다.
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for d in range(4):
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if 0<=nx<4 and 0<=ny<4:
            next_num = num*10 + board[nx][ny] # 숫자를 이어 붙여주기 위한 코드
            move(k+1, nx, ny, result, next_num)

for tc in range(int(input())):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            move(1, i, j, result, board[i][j])
    print('#{} {}'.format(tc+1, len(result)))