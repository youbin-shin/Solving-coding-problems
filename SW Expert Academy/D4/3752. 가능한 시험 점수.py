for tc in range(int(input())):
    N = int(input())
    scores = list(map(int, input().split()))
    result = set([0])
    for i in scores:
        num = set()
        for j in result:
            num.add(i+j)
        result = set(list(result) + list(num))
    print('#{} {}'.format(tc+1, len(list(result))))