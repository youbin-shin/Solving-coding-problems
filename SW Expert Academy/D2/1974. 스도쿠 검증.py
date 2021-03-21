for t in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):

        row = [0] * 10
        col = [0] * 10
        for j in range(9):
           if row[arr[i][j]] == 1 or col[arr[j][i]] == 1:
               ans = 0
               break
           row[arr[i][j]] = 1
           col[arr[j][i]] = 1

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            c = [0] * 10
            for i in range(3):
                for j in range(3):
                    if c[arr[i+x][j+y]] == 1:
                        ans = 0
                        break
                    c[arr[i+x][y+j]] = 1


    print('#{} {}'.format(t+1,ans))