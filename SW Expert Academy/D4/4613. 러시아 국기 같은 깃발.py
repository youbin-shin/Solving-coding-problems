for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = N*M
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            cnt = 0
            for r in range(0, i+1):
                for c in range(M):
                    if arr[r][c] != 'W': cnt += 1
            for r in range(i+1, j+1):
                for c in range(M):
                    if arr[r][c] != 'B': cnt += 1

            for r in range(j+1, N):
                for c in range(M):
                    if arr[r][c] != 'R': cnt += 1
            ans = min(ans, cnt)
    print('#{} {}'.format(t+1,ans))