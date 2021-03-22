T = 10
for tc in range(T):
    N = int(input())
    magnetics = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if magnetics[j][i] == 1:
                break
            elif magnetics[j][i] == 2:
                magnetics[j][i] = 0

    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if magnetics[j][i] == 2:
                break
            elif magnetics[j][i] == 1:
                magnetics[j][i] = 0

    ans = 0
    for i in range(N):
        result = []
        for j in range(N):
            if magnetics[j][i] != 0:
                if result == []:
                    result.append(magnetics[j][i])
                elif result[-1] != magnetics[j][i]:
                    result.append(magnetics[j][i])
        if len(result) > 1:
            ans += len(result) // 2
            
    print('#{} {}'.format(tc+1, ans))