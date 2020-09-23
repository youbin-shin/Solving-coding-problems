def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(str(n))):
        answer += int(n[i])
    return answer


# n = 123
# print(solution(n))