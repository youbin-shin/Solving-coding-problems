tc = int(input())
for tc in range(tc):
    n = int(input())
    ndlst = [0 for _ in range(n)]
    nlst = list(map(int, input().split()))
    for i in range(n):
        ndlst[i] = nlst[2 * i:2 * i + 2]


    mayfirst = []
    first = 0

    for j in set(nlst):
        if nlst.count(j)==1:
            mayfirst.append(j)

    for x in range(len(ndlst)):
        if ndlst[x][0] in mayfirst:
            first = ndlst[x][0]

    result = []

    for a in range(len(ndlst)):
        if ndlst[a][0] == first:
            result.append(ndlst[a])

    while True:
        if len(result) == len(ndlst):
            break
        for c in range(len(ndlst)):
            if result[-1][-1] == ndlst[c][0]:
                result.append(ndlst[c])


    # 출력
    print('#{} '.format(tc+1), end='')
    for i in range(n):
        for j in range(2):
            print(result[i][j], end=' ')

    print()