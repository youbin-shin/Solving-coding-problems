T = int(input())

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[j][i] != 0:
                cnt += 1
                if i == N-1:
                    result.append(cnt)
            elif board[j][i] == 0 and cnt != 0:
                result.append(cnt)
                cnt = 0

    result.sort()
    f_result = []
    mul = []
    for k in set(result):
        f_result.append([result.count(k) * k, k, result.count(k)])
        mul.append(result.count(k) * k)

    ans = []
    mul_idx = sorted(set(mul))
    for i in mul_idx:
        for j in range(len(f_result)):
            if i == f_result[j][0]:
                ans.append(f_result[j][1])
                ans.append(f_result[j][2])

    ans = ' '.join(map(str, ans))
  
    print('#{} {} {}'.format(t+1, len(f_result), ans))