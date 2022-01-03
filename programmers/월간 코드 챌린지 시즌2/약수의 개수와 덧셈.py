def solution(left, right):
    answer = 0
    for num in range(left, right + 1, 1):
        num_cnt = len([i for i in range(1, num + 1) if num % i == 0])
        if num_cnt % 2:
            answer -= num
        else:
            answer += num
    return answer