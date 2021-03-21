for t in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    ans = -100000
    for i in range(M-N+1):
        sum = 0
        for j in range(N):
            sum += A[j]*B[i+j]
        if ans < sum:
            ans = sum

    print('#{} {}'.format(t+1, ans))