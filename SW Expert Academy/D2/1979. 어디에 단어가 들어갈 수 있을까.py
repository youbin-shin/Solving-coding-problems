T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로 확인
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                temp += 1
                if j < N-1 and puzzle[i][j+1] == 0 and temp==K:
                    result += 1
                elif j == N-1 and temp == K:
                    result += 1
            else:
                temp = 0

    # 세로 확인
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                temp += 1
                if j < N-1 and puzzle[j+1][i] == 0 and temp==K:
                    result += 1
                elif j == N-1 and temp == K:
                    result += 1
            else:
                temp = 0


    print('#{} {}'.format(tc+1, result))