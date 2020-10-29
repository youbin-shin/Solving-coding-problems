def solution(num):
    answer = 0
    while num != 1:
        if answer > 500:
            answer = -1
            break
        if num % 2: # 홀수인 경우
            num = num * 3 + 1
        else: # 짝수인 경우
            num = int(num // 2)
        answer += 1
    return answer