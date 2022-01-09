def solution(n, left, right):
    answer = []
    for num in range(left, right + 1):
        q, r = divmod(num, n)
        answer.append(max(q, r) + 1)
    return answer