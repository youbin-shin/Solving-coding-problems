for t in range(int(input())):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M):
                for k2 in range(M):
                    catch += fly[i+k][j+k2]
            ans = max(catch, ans)
            
    print('#{} {}'.format(t+1, ans))