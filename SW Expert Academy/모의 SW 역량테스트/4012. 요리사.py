def comb(lst, n): # lst에서 n개를 택하는 조합만들어 주는 함수
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


for tc in range(int(input())):
    N = int(input())
    Slst = [list(map(int, input().split())) for _ in range(N)]
    fresult = 9999999999
    R = N//2
    Alsts = comb([i for i in range(N)], R)
    for i in range(len(Alsts)):
        Alst = Alsts[i] # A에 들어갈 식재료 인덱스 저장
        Blst = []
        for j in range(N):
            if j not in Alst:
                Blst.append(j) # B에 A 외의 식재료 인덱스 저장
        result = 0

        # 식재료에서 2개를 택하는 조합 리스트를 저장한다.
        A = comb(Alst, 2)
        B = comb(Blst, 2)
        for k in range(len(A)):
            # 시너지 합의 차이를 더해준다.
            result += Slst[A[k][0]][A[k][1]] + Slst[A[k][1]][A[k][0]] - Slst[B[k][0]][B[k][1]] - Slst[B[k][1]][B[k][0]]
        # 맛의 차이가 최소인 경우를 구하기 위해 if문을 이용한다.
        if fresult > abs(result):
            fresult = abs(result)
    print('#{} {}'.format(tc+1, fresult))