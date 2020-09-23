def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)-1, -1, -1):
        answer.append(int(n[i]))
    return answer


# n = 12345
# print(solution(n))