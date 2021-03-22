T = 10
for tc in range(T):
    N = int(input())
    palindrome = [list(map(str,input())) for _ in range(8)]
    cnt = 0

    # 가로 회문 확인
    for i in range(8):
        for j in range(9-N):
            word = ''
            for k in range(N):
                word += palindrome[i][j+k]
            if word == word[::-1]:
                cnt += 1

    # 세로 회문 확인
    for j in range(8):
        for i in range(9 - N):
            word = ''
            for k in range(N):
                word += palindrome[i+k][j]
            if word == word[::-1]:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))