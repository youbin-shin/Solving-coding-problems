for t in range(int(input())):
    arr = [['-1']*15 for _ in range(5)]
    ans = ''
    for i in range(5):
        inputV = input()
        for j in range(len(inputV)):
            arr[i][j] = inputV[j]
    for j in range(15):
        for i in range(5):
            if arr[i][j] == '-1':
                pass
            else:
                ans += arr[i][j]
    print('#{} {}'.format(t+1, ans))