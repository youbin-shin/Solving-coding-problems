for t in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    lst = []

    for i in range(N):
        for j in range(i+1, N):
            num = str(A[i]*A[j])
            for k in range(len(num)-1):
                if int(num[k]) > int(num[k+1]):
                    break
            else:
                lst.append(int(num))
    lst.sort()

    if len(lst) == 0:
        result = -1
    else:
        result = lst[-1]
    print('#{} {}'.format(t, result))