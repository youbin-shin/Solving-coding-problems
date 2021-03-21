T = int(input())
for tc in range(T):
    N = input()
    numlst = [0]*10

    k = 0
    while numlst.count(0) != 0:
        k += 1
        Nk = str(int(N) * k)
        for i in Nk:
            numlst[int(i)] += 1

    print('#{} {}'.format(tc+1, Nk))