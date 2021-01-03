def solution(s):
    answer = False
    plusCheck = True
    check = []
    for i in s:
        # "(" 인 경우
        if i == "(":
            check.append(i)

        # ")" 인 경우
        if len(check) == 0 and i == ")": # 무조건 false 인 경우
            plusCheck = False
            break
        elif check and check[-1] == "(" and i == ")": # 괄호 짝이 맞으면 check list 끝 제거
            check.pop()

    if plusCheck and len(check) == 0:
        answer = True
    return answer


# s = "(()("
# print(solution(s))