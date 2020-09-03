def solution(n):
    memo = [True] * (n + 1) # True 설정 => 소수

    # n의 최대 약수는 sqrt(n) 이하이기에 sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if memo[i] == True:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i이후 i의 배수들을 False 판정
                memo[j] = False

    return len([i for i in range(2, n+1) if memo[i] == True])