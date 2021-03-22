for t in range(1, int(input()) + 1):
    N = int(input())
    crops = [list(map(int, input())) for _ in range(N)]
    ans = sum(crops[N//2])

    plus = N
    start = 0
    for i in range(N//2-1, -1, -1):
        plus -= 2
        start += 1
        for j in range(plus):
            ans += crops[i][start+j]
            ans += crops[N-i-1][start+j]

    print('#{} {}'.format(t, ans))