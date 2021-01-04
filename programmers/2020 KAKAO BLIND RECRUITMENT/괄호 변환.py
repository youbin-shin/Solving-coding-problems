# 2번 과정 : 균형잡힌 괄호 문자열 u, v로 분리하는 함수
def divide(w):
    openCnt = 0
    closeCnt = 0
    for i in range(len(w)):
        if w[i] == "(":
            openCnt += 1
        else:
            closeCnt += 1
        if openCnt == closeCnt:
            return w[:i + 1], w[i + 1:]


# 3번 과정 : 올바른 괄호 문자열인지 확인
def check(u):
    temp = []
    frag = True
    for i in range(len(u)):
        if u[i] == "(":
            temp.append("(")
        elif temp == [] and u[i] == ")":
            frag = False
            break
        elif temp and temp[-1] == "(" and u[i] == ")":
            temp.pop()
    if temp != []:
        frag = False
    return frag


def solution(p):
    # 1번 과정
    if p == "":
        return ""
    # 2번 과정
    u, v = divide(p)
    # 3번 과정
    if check(u):
        v = solution(v) # 3-1
        answer = u + v
    # 4번 과정
    else:
        answer = "(" # 4-1
        v = solution(v) # 4-2
        answer += v + ")" # 4-3
        # 4-4
        # 주의 사항 : 역순이아니라 괄호 방향이 바뀌는 것!
        u = u[1:-1]
        uChange = ""
        for uc in u:
            if uc == "(":
                uChange += ")"
            else:
                uChange += "("
        answer += uChange
    return answer # 4-5


# p = "(()())()"
# p = "())("
# p = "()))((()"
# p = ")()("
# print(solution(p))