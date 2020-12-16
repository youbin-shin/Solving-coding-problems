import math

def solution(n,a,b):
    answer = 0
    while a != b: # a, b 가 같은 경기를 하지 않는 경우
        a, b = math.ceil(a / 2), math.ceil(b / 2) # 다음 경기에 참가하게 될 경기 번호로 변경
        answer += 1
    return answer

# print(solution(8, 4, 7))