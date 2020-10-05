def solution(n, m):
    num = max(n, m)
    answer = []
    for i in range(num, -1, -1):
        if (n % i == 0) and (m % i == 0):
            answer.append(i)
            answer.append(i * int(n // i) * int(m // i))
            break
    return answer


# n = 3
# m = 12
# print(solution(n, m))
