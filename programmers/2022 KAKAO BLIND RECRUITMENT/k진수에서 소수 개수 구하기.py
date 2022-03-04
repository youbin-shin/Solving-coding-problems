from math import sqrt


def solution(n, k):
    answer = 0
    next_n = ""
    while n:
        q, r = divmod(n, k)
        next_n = str(r) + next_n
        n = q
    n_list = list(map(str, next_n.split("0")))
    for nl in n_list:
        if nl == "":
            continue
        nl = int(nl)
        flag = True if nl != 1 else False
        # (소수 체크) 제곱근으로 확인하여 시간 초과 해결
        for i in range(2, int(sqrt(nl) + 1)): 
            if nl % i == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer
