def solution(n):
    answer = n + 1
    num = 1
    while num < n:
        if n % num == 1:
            answer = num
            break
        num += 1
    return answer