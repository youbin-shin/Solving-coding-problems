def solution(n):
    answer = ''
    k = 0
    while k != n:
        if k % 2: answer += "박"
        else: answer += "수"
        k += 1
    return answer