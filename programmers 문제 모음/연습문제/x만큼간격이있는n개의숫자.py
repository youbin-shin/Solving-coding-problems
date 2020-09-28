def solution(x, n):
    answer = [x]
    for i in range(n-1):
        answer.append(answer[i] + x)
    return answer