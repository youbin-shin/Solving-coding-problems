for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    vote = [0] * N
    B = list(map(int, input().split()))

    for b in B:
        for i in range(N):
            if A[i] <= b:
                vote[i] += 1
                break
    print(vote)

    print('#{} {}'.format(t, vote.index(max(vote))+1))