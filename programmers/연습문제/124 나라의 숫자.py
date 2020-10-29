def solution(n):
    num = [4, 1, 2]
    answer = 0
    idx = 1
    while n > 0:
        r = n % 3
        n = n // 3
        if r == 0: n -= 1
        answer += idx*num[r]
        idx *= 10
    return answer

# n = 3
# print(solution(n))