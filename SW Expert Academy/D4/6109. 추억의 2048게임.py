testcase = int(input())

def rotate(lst,N): # 90도 방향으로 회전
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = lst[N-j-1][i]
    return result

for tc in range(testcase):
    num, action = map(str, input().split())
    N = int(num)
    lst = [[0 for _ in range(N)] for _ in range(N)]
    result = [[0 for _ in range(0)] for _ in range(N)]
    for i in range(N):
        lst[i] = list(map(int, input().split()))

    if action == 'up':
        lst = rotate(rotate(rotate(lst, N),N),N)
    elif action == 'down':
        lst = rotate(lst, N)
    elif action == 'right':
        lst = rotate(rotate(lst,N),N)


    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                pass
            else:
                result[i].append(lst[i][j])
        while len(result[i]) < N:
            result[i].append(0)


    #2048 숫자 계산 코드
    for i in range(N):
        for j in range(N-1):
            if result[i][j] == result[i][j+1]:
                result[i][j] *= 2
                for k in range(j+1, N-1):
                    result[i][k] = result[i][k+1]
                result[i][N-1] = 0

    if action == 'up':
        result = rotate(result, N)
    elif action == 'down':
        result = rotate(rotate(rotate(result, N),N),N)
    elif action == 'right':
        result = rotate(rotate(result,N),N)

    print('#{}'.format(tc+1))
    # 출력시 사용
    for i in range(N):
        for j in range(N):
            print(result[i][j], end=' ')
        print()