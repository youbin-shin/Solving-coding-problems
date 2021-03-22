for tc in range(10):
    testnum = int(input())
    board = [list(map(str, input())) for _ in range(100)]
    longest = 0

    # 가로 탐색
    for i in range(100):
        for j in range(100):
            word = ''
            for k in range(99-j, -1, -1):
                word += board[i][k]
                if word == word[::-1] and len(word) > longest:
                    longest = len(word)
                    break

    # 세로 탐색
    for j in range(100):
        for i in range(100):
            word = ''
            for k in range(99-i, -1, -1):
                word += board[k][j]
                if word == word[::-1] and len(word) > longest:
                    longest = len(word)
                    break

    print('#{} {}'.format(testnum, longest))