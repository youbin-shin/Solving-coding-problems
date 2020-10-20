from datetime import datetime

def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    before = datetime(2016, 1, 1)
    after = datetime(2016, a, b)
    diff = (after - before).days 
    answer = day[diff % 7]
    return answer


# a = 5
# b = 24
# print(solution(a, b))
