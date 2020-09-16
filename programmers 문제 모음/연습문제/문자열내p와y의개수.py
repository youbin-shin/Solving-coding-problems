def solution(s):
    s = list(s.lower())
    p_cnt = s.count("p")
    y_cnt = s.count("y")
    if p_cnt == y_cnt: answer = True
    else: answer = False
    return answer