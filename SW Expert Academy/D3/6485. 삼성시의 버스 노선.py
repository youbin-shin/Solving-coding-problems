T = int(input())
for t in range(T):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    buslines = [0] * 5001
    for i in range(N):
        for j in range(bus[i][0], bus[i][1]+ 1):
            buslines[j] += 1

    result = ''
    P = int(input())
    for _ in range(P):
        result += str(buslines[int(input())]) + ' '
    print('#{} {}'.format(t+1, result))