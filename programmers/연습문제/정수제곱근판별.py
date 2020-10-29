import math

def solution(n):
    answer = -1
    m = int(math.sqrt(n))
    if m * m == n: answer = (m+1) * (m+1)
    return answer