for t in range(int(input())):
    W, H, N = map(int, input().split())
    cnt = 0
    x, y = map(int, input().split())
    for i in range(N-1):
        xn, yn = map(int, input().split())
        dx = x - xn
        dy = y - yn
        if dy*dx > 0:
            cnt += max(abs(dx), abs(dy))
        else:
            cnt += abs(dx) + abs(dy)
        x, y = xn, yn

    print('#{} {}'.format(t+1, cnt))