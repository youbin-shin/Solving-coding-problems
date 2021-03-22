for i in range(10):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    tc = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    # 계산
    ## 가로줄
    sum_1 = sum(arr[0])
    for i in range(1, 100):
        if sum_1 < sum(arr[i]):
            sum_1 = sum(arr[i])

    ## 세로줄
    for i in range(100):
        sum_2 += arr[i][0]
    for i in range(1, 100):
        sum_2_sample = 0
        for j in range(100):
            sum_2_sample += arr[j][i]
            if sum_2 < sum_2_sample:
                sum_2 = sum_2_sample

    ## 대각선
    sum_3_sample = 0
    for i in range(100):
        sum_3 += arr[i][i]
        sum_3_sample += arr[i][99-i]
    sum_3 = max(sum_3_sample, sum_3)

    result = max(sum_2, sum_1, sum_3)

    print('#{} {}'. format(tc, result))