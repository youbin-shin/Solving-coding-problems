def solution(n):
    num = [0, 1]
    while len(num) < n + 1: # n번째까지 피보나치 수 만들기
        num.append(num[-1] + num[-2])
    answer = num[n] % 1234567
    return answer

n = 3
print(solution(n))