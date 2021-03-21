testcase = int(input())
for tc in range(1, testcase + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    top = arr[-1]

    for i in range(N - 1, -1, -1):
        if arr[i] < top:
            sum += top - arr[i]
        else:
            top = arr[i]

    print('#{} {}'.format(tc, sum))